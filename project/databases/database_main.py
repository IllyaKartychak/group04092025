import config
import psycopg2

with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS topics (
                id SERIAL PRIMARY KEY,
                chat_description VARCHAR(50) NOT NULL UNIQUE
            )
        """
        cursor.execute(query)

        query2 = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(75) NOT NULL,
                surname VARCHAR(75) NOT NULL
                
            );

            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                post VARCHAR(75) NOT NULL,
                user_id INTEGER REFERENCES users(id),
                topic_id INTEGER REFERENCES topics(id)
            );
        """
        cursor.execute(query2)

# CREATE
with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query_insert = 'INSERT INTO topics (chat_description) VALUES (%s)'
        cursor.execute(query_insert, ("weather", ))
