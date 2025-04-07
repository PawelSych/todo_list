from flask import request, jsonify
from db import get_connection

def register_routes(app):
    @app.route('/tasks/<int:task_id>/complete', methods=['PUT'])
    def mark_task_completed(task_id):
        data = request.get_json()
        completed = data.get('completed')

        if completed is None:
            return jsonify({"error": "Missing 'completed' field"}), 400

        if not isinstance(completed, bool):
            return jsonify({"error": "'completed' must be true or false (boolean)"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET completed = %s, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """, (completed, task_id))

        conn.commit()
        rows_updated = cursor.rowcount

        cursor.close()
        conn.close()

        if rows_updated == 0:
            return jsonify({"message": "Task not found"}), 404

        return jsonify({"message": "Task marked as completed"}), 200
