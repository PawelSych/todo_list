from flask import Flask
import addTask
import getTasks
import addUser  # jeśli masz już ten plik

app = Flask(__name__)

# Rejestracja endpointów
addTask.register_routes(app)
getTasks.register_routes(app)
addUser.register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
