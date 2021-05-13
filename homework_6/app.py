import psycopg2

"""
    - *dbname*: the database name
    - *database*: the database name
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address
    - *port*: connection port number
"""
pg_creds = {
    'host': '172.16.148.2',
    'port': '5432',
    'database': 'postgres',
    'user': 'pguser',
    'password': 'secret'
}


def get_data():
    with psycopg2.connect(**pg_creds) as pg_connection:
        cursor = pg_connection.cursor()
        cursor.execute('select * from film')
        result = cursor.fetchall()
        print(result)


if __name__ == '__main__':
    get_data()
