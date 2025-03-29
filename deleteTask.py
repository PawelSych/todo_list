from flask import jsonify
from db import get_connection

def register_routes(app):
    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = :id", {"id": task_id})
        conn.commit()

        rows_deleted = cursor.rowcount

        cursor.close()
        conn.close()

        if rows_deleted == 0:
            return jsonify({"message": "Task not found"}), 404

        return jsonify({"message": "Task deleted successfully"}), 200
