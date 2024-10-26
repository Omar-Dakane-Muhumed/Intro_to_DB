
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
            print("Database 'alx_book_store' created successfully or already exists!")

            # Check if the database exists
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            if ('alx_book_store',) in databases:
                print("Confirmation: Database 'alx_book_store' exists.")
            else:
                print("Error: Database 'alx_book_store' could not be confirmed.")

    except mysql.connector.Error as e:
        if e.errno == 1045:
            print("Access denied: Check your username or password.")
        elif e.errno == 2003:
            print("Can't connect to MySQL server on the specified host.")
        else:
            print(f"Unexpected error occurred: {e}")

    finally:
        # Close the cursor and connection to free resources
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        except NameError:
            print("Connection was not established, so there's nothing to close.")

if __name__ == "__main__":
    create_database()

