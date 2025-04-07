from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL connection
def get_connection():
    connection = psycopg2.connect(
        dbname='mydb',
        user='postgres',
        password='rootuser1',
        host='localhost',
        port='5432'
    )
    return connection

# Endpoint to fetch all users
@app.route('/users')
def users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    # Convert rows to list of dictionaries
    result = [dict(zip(colnames, row)) for row in rows]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
