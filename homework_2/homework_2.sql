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
ORDER BY f.title

-- вывести топ 3 актеров, которые больше всего появлялись в фильмах в категории “Children”. Если у нескольких актеров одинаковое кол-во фильмов, вывести всех..

-- вывести города с количеством активных и неактивных клиентов (активный — customer.active = 1). Отсортировать по количеству неактивных клиентов по убыванию.
-- вывести категорию фильмов, у которой самое большое кол-во часов суммарной аренды в городах (customer.address_id в этом city), и которые начинаются на букву “a”. То же самое сделать для городов в которых есть символ “-”. Написать все в одном запросе.
