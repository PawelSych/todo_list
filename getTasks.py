from flask import request, jsonify
from db import get_connection

def register_routes(app):
    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        user_id = request.args.get('user_id')

        if not user_id:
            return jsonify({"error": "Missing user_id parameter"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, title, priority, completed, created_at, updated_at
            FROM tasks
            WHERE user_id = %s
        """, (user_id,))

        rows = cursor.fetchall()
        tasks = []

        for row in rows:
            tasks.append({
                "id": row[0],
                "title": row[1],
                "priority": row[2],
                "completed": bool(row[3]),
                "created_at": str(row[4]),
                "updated_at": str(row[5])
            })

        cursor.close()
        conn.close()

        if not tasks:
            return jsonify({"message": "No tasks found"}), 404

        return jsonify(tasks), 200
