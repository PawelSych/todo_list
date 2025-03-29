from flask import Flask, jsonify, request
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

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

# validation if fields are empty or not
    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400 # code 400 is "Bad request"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, email, password, created_at)
        VALUES (:username, :email, :password, SYSDATE)
    """, {
        "username": "testdodania",
        "email": "testdodania@gmail.com",
        "password": "testpassword"
    })

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "User created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
