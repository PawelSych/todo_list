from flask import Flask, request, jsonify
import oracledb

app = Flask(__name__)

# Funkcja łączenia z bazą Oracle
def get_connection():
    connection = oracledb.connect(
        user='pawel',
        password='rootuser1',
        dsn='localhost:1521/XEPDB1'
    )
    return connection

# Endpoint do dodawania nowego zadania
@app.route('/newtask', methods=['POST'])
def add_task():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')         # lub 'name', jeśli tak masz w JSON
    priority = data.get('priority')

    # Walidacja danych wejściowych
    if not user_id or not title or not priority:
        return jsonify({"error": "Missing fields"}), 400

    # Połączenie z bazą danych i wykonanie zapytania INSERT
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

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)
