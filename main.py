## TEST REPO, DB IS NOT COMPLETED YET


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model bazy danych dla użytkowników
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Model bazy danych dla zadań
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Endpoint do pobierania listy zadań użytkownika
@app.route('/tasks', methods=['GET'])
def get_user_tasks():
    user_id = request.args.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'Missing user_id parameter'}), 400

    tasks = Task.query.filter_by(user_id=user_id).all()

    if not tasks:
        return jsonify({'message': 'No tasks found for the user'}), 404

    tasks_list = [
        {
            'id': task.id,
            'name': task.name,
            'priority': task.priority,
            'completed': task.completed
        }
        for task in tasks
    ]

    return jsonify({'tasks': tasks_list}), 200

if __name__ == '__main__':
    app.run(debug=True)
