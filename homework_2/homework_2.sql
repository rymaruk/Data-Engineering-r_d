-- Используя демо базу данных, напишите запросы для того, чтобы:
--
-- вывести количество фильмов в каждой категории, отсортировать по убыванию.
SELECT c.name as "Category", count(fc.category_id) as "Quantity films"
FROM  film_category fc
    LEFT JOIN category c ON c.category_id = fc.category_id
GROUP BY fc.category_id, c.name
ORDER BY 2 DESC;

-- вывести 10 актеров, чьи фильмы большего всего арендовали, отсортировать по убыванию.
SELECT concat(a.first_name, ' ', a.last_name) as "Actor", f.rental_rate as "Rental rate"
FROM film f
    LEFT JOIN film_actor fa ON f.film_id = fa.film_id
        LEFT JOIN actor a ON fa.actor_id = a.actor_id
GROUP BY a.first_name, f.rental_rate, a.last_name
ORDER BY f.rental_rate DESC
LIMIT 100;

-- вывести категорию фильмов, на которую потратили больше всего денег.
SELECT p.rental_id as "Category ID", c.name as "Category", sum(p.amount) as "Total"
FROM payment p
    JOIN rental r ON p.rental_id = r.rental_id
        JOIN inventory i ON r.inventory_id = i.inventory_id
            JOIN film f ON i.film_id = f.film_id
                JOIN film_category fc ON f.film_id = fc.film_id
                    JOIN category c ON fc.category_id = c.category_id
GROUP BY p.rental_id, c.name
ORDER BY 3 DESC
LIMIT 1;

-- вывести названия фильмов, которых нет в inventory. Написать запрос без использования оператора IN.
SELECT f.title as "Films" FROM film f
    LEFT JOIN inventory i
        ON f.film_id = i.film_id
            WHERE i.film_id IS NULL
ORDER BY f.title;

-- вывести топ 3 актеров, которые больше всего появлялись в фильмах в категории “Children”. Если у нескольких актеров одинаковое кол-во фильмов, вывести всех..
SELECT c.name as "Category", count(f.film_id) as "Quantity films", concat(a.first_name, ' ', a.last_name) as "Name"
FROM category c
    LEFT JOIN film_category fc on c.category_id = fc.category_id
        LEFT JOIN film f ON f.film_id = fc.film_id
            LEFT JOIN film_actor fa ON f.film_id = fa.film_id
                LEFT JOIN actor a ON a.actor_id = fa.actor_id
WHERE c.name = 'Children' AND f.film_id = fc.film_id
GROUP BY c.category_id, "Name"
ORDER BY 2 DESC
LIMIT 3;

-- вывести города с количеством активных и неактивных клиентов (активный — customer.active = 1). Отсортировать по количеству неактивных клиентов по убыванию.
SELECT c.city as "City", count(cus1.active) as "Active", count(cus2.active) as "Inactive" FROM city c
    LEFT JOIN address a ON a.city_id = c.city_id
        LEFT JOIN customer cus1 ON (a.address_id = cus1.address_id AND cus1.active = 1)
            LEFT JOIN customer cus2 on (a.address_id = cus2.address_id AND cus2.active = 0)
GROUP BY c.city
ORDER BY 3 DESC;



-- вывести категорию фильмов, у которой самое большое кол-во часов суммарной аренды в городах (customer.address_id в этом city), и которые начинаются на букву “a”. То же самое сделать для городов в которых есть символ “-”. Написать все в одном запросе.
SELECT p.rental_id as "Category ID", c.name as "Category", ci.city as "City", date_part('hours', r.return_date - r.rental_date) as "Rental hours"
FROM payment p
    JOIN rental r ON p.rental_id = r.rental_id AND r.return_date IS NOT Null

        JOIN customer cus ON r.customer_id = cus.customer_id
            JOIN address add ON add.address_id = cus.address_id
                JOIN city ci ON ci.city_id = add.city_id

                    JOIN inventory i ON r.inventory_id = i.inventory_id
                        JOIN film f ON i.film_id = f.film_id
                            JOIN film_category fc ON f.film_id = fc.film_id
                                JOIN category c ON fc.category_id = c.category_id

WHERE c.name LIKE 'A%' AND ci.city LIKE '%-%'
GROUP BY r.return_date, r.rental_date, p.rental_id, ci.city, c.name
ORDER BY 4 DESC
LIMIT 1;
