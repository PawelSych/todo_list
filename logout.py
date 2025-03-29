from flask import request, jsonify
from db import get_connection

def register_routes(app):
    @app.route('/logout', methods=['POST'])
    def logout():
        data = request.get_json()
        token = data.get('token')

        if not token:
            return jsonify({"error": "Missing token"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM sessions
            WHERE token = :token
        """, {"token": token})

        conn.commit()
        rows_deleted = cursor.rowcount

        cursor.close()
        conn.close()

        if rows_deleted == 0:
            return jsonify({"message": "Session not found"}), 404

        return jsonify({"message": "User logged out successfully"}), 200
