from flask import request, jsonify
from db import get_connection
import uuid
import datetime

def register_routes(app):
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"error": "Missing credentials"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, password FROM users WHERE username = :username
        """, {"username": username})
        user = cursor.fetchone()

        if not user:
            cursor.close()
            conn.close()
            return jsonify({"error": "Invalid username or password"}), 401

        user_id, db_password = user

        if password != db_password:
            cursor.close()
            conn.close()
            return jsonify({"error": "Invalid username or password"}), 401

        token = str(uuid.uuid4())
        now = datetime.datetime.now()
        expires = now + datetime.timedelta(hours=1)

        cursor.execute("""
            INSERT INTO sessions (user_id, token, created_at, expires_at)
            VALUES (:user_id, :token, :created_at, :expires_at)
        """, {
            "user_id": user_id,
            "token": token,
            "created_at": now,
            "expires_at": expires
        })

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"token": token}), 200
