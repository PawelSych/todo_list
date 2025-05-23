from flask import Flask
import addTask
import getTasks
import addUser  # jeśli masz już ten plik
import deleteTask
import completeTask
import logout
import login
import updatePriority

app = Flask(__name__)

# Rejestracja endpointów
addTask.register_routes(app)
getTasks.register_routes(app)
addUser.register_routes(app)
deleteTask.register_routes(app)
completeTask.register_routes(app)
logout.register_routes(app)
login.register_routes(app)
updatePriority.register_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
