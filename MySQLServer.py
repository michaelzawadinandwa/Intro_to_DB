#!/usr/bin/python3
import MySQLdb

def create_database():
    db = None
    cursor = None

    try:
        # Attempt to connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="root"
        )

        cursor = db.cursor()

        try:
            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

        except Exception as sql_error:
            print("Error: Failed to create the database.")
            print(f"Reason: {sql_error}")

    except Exception as conn_error:
        print("Error: Unable to connect to the MySQL server.")
        print(f"Reason: {conn_error}")

    finally:
        # Safely close cursor and connection
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass

        if db is not None:
            try:
                db.close()
            except Exception:
                pass


if __name__ == "__main__":
    create_database()
