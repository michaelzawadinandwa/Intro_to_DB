#!/usr/bin/python3
import MySQLdb

def create_database():
    try:
        # Connect to MySQL server (NOT to any specific database yet)
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="root"
        )

        cursor = db.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        print("Error: Unable to connect to the MySQL server.")
        return

    finally:
        # Ensure DB closes safely
        try:
            cursor.close()
            db.close()
        except:
            pass


if __name__ == "__main__":
    create_database()
