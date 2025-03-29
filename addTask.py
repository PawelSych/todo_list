from flask import request, jsonify
from db import get_connection

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
            VALUES (:user_id, :title, :priority, 0, SYSDATE, SYSDATE)
        """, {
            "user_id": user_id,
            "title": title,
            "priority": priority
        })

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Task created successfully"}), 201
