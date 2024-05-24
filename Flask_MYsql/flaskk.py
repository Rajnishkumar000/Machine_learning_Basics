from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Establishing a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raj@12345",
    database="college"
)

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

@app.route('/fetch_data')
def fetch_data():
    try:
        # Executing SQL query
        cursor.execute("SELECT * FROM student")

        # Fetching all the rows using fetchall() method
        rows = cursor.fetchall()

        # Converting rows to a list of dictionaries
        data = []
        for row in rows:
            data.append({
                'column1': row[0],
                'column2': row[1],
                # Add more columns as needed
            })

        # Returning JSON response
        return jsonify({'data': data})

    except mysql.connector.Error as e:
        # Handling errors
        return jsonify({'error': 'Error reading data from MySQL table: {}'.format(e)}), 500

@app.route('/')
def index():
    return

if __name__ == '__main__':
    app.run(debug=True)
