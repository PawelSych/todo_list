from flask import request, jsonify
from db import get_connection  # zakładam, że masz już psycopg2/psycopg lub podobny

def register_routes(app):
    @app.route('/newtask', methods=['POST'])
    def add_task():
        data = request.get_json()
        user_id = data.get('user_id')
        title = data.get('title')
        priority = data.get('priority')

        if not user_id or not title or not priority:
            return jsonify({"error": "Missing fields"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks (user_id, title, priority, completed, created_at, updated_at)
            VALUES (%s, %s, %s, FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """, (user_id, title, priority))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Task created successfully"}), 201
