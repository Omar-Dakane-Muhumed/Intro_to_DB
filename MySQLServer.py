

import mysql.connector

# Establish the database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Omar123@"
)

cursor = db_connection.cursor()

# Read and execute SQL file
with open("alx_book_store.sql", "r") as file:
    sql_commands = file.read()
    for command in sql_commands.split(';'):
        if command.strip():
            cursor.execute(command)

db_connection.commit()
print("Database setup successfully.")
cursor.close()
db_connection.close()

