import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # CONNECT TO MYSQL SERVER (edit user/password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""   # <-- Add your MySQL password here
        )

        # Check connection success
        if connection.is_connected():
            cursor = connection.cursor()

            # Create database safely
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor if it was opened
        if cursor is not None:
            cursor.close()

        # Close connection safely
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
