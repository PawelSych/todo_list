from flask import request, jsonify
from db import get_connection

def register_routes(app):
    @app.route('/users', methods=['POST'])
    def add_user():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"error": "Missing fields"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (username, email, password, created_at)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
        """, (username, email, password))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "User created successfully"}), 201
