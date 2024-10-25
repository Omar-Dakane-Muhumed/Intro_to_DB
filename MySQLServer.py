import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Update this with your MySQL server host if different
            user='root',  # Replace with your MySQL username
            password='Omar123@'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection to free resources
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_database()

