from flask import Flask, jsonify
import oracledb

app = Flask(__name__)

# Function to create Oracle database connection
def get_connection():
    connection = oracledb.connect(
        user='pawel',
        password='rootuser1',
        dsn='localhost:1521/XEPDB1'
    )
    return connection

# Endpoint to fetch all data from USERS table
@app.route('/users')
def users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM USERS')
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    # Convert the rows to JSON
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
