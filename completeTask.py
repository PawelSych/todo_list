from flask import request, jsonify
from db import get_connection

def register_routes(app):
    @app.route('/tasks/<int:task_id>/priority', methods=['PUT'])
    def update_priority(task_id):
        data = request.get_json()
        priority = data.get('priority')

        if priority not in [1, 2, 3]:
            return jsonify({"error": "Priority must be 1 (low), 2 (medium), or 3 (high)"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET priority = :priority, updated_at = SYSDATE
            WHERE id = :task_id
        """, {
            "priority": priority,
            "task_id": task_id
        })

        conn.commit()
        rows_updated = cursor.rowcount

        cursor.close()
        conn.close()

        if rows_updated == 0:
            return jsonify({"message": "Task not found"}), 404

        return jsonify({"message": "Task priority updated"}), 200
