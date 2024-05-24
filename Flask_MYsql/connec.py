import mysql.connector

# Establishing a connection to the MySQL database
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Raj@12345",
#     database="college"
# )

connection = mysql.connector.connect(
    host="localhost",
    user="RajnishKumar",
    password="RajnishKumar121",
    database="college"
)

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

try:
    # Executing SQL query
    cursor.execute("SELECT * FROM student")

    # Fetching all the rows using fetchall() method
    rows = cursor.fetchall()

    # Iterating over the rows and printing each row
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    # Handling errors
    print("Error reading data from MySQL table:", e)

finally:
    # Closing the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
