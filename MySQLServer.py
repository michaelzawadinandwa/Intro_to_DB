import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL Server (update with your username/password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""   # <-- Put your MySQL password here
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                connection.commit()
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                connection.rollback()
                print(f"Error executing CREATE DATABASE: {e}")
                raise

    except mysql.connector.ProgrammingError as e:
        print(f"Programming Error: {e}")
    except mysql.connector.OperationalError as e:
        print(f"Operational Error: {e}")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Close cursor safely
        if cursor is not None:
            try:
                cursor.close()
            except Error as e:
                print(f"Error closing cursor: {e}")
        
        # Close connection safely
        if connection is not None and connection.is_connected():
            try:
                connection.close()
                print("MySQL connection closed.")
            except Error as e:
                print(f"Error closing connection: {e}")

if __name__ == "__main__":
    try:
        create_database()
    except Exception as e:
        print(f"Fatal error in main: {e}")
