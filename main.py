import psycopg2 as db


class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database="tele_test_bot",
            user="postgres",
            host="localhost",
            password="postgres"
        )
        cursor = database.cursor()
        cursor.execute(query)
        if query_type == "insert":
            database.commit()
            return "inserted"
        
        if query_type == "select":
            return cursor.fetchall()
