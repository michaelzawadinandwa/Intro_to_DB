# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no database specified)
        connection = mysql.connector.connect(
            host="localhost",   # Change if needed
            user="root",        # Change to your MySQL username
            password=""         # Change to your MySQL password
        )

        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection safely
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
