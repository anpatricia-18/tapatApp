import requests
from flask import Flask, jsonify, request

# Ejemplo de datos (deberías usar una base de datos real en un entorno de producción)
users = [
    {"id": 1, "username": "mare", "password": "12345", "email": "prova2@gmail.com", "role": "cuidador"},
    {"id": 2, "username": "pare", "password": "54321", "email": "drsmith@example.com", "role": "metge"}
]

children = [
    {"id": 1, "name": "Child 1", "sleep_average": 8, "treatment": "Treatment A", "time": 3},
    {"id": 2, "name": "Child 2", "sleep_average": 7, "treatment": "Treatment B", "time": 4}
]

relation_user_child = [
    {"user_id": 1, "child_id": 1},
    {"user_id": 1, "child_id": 2}
]

# Inicializamos la app Flask
app = Flask(__name__)

# Endpoints para cada entidad
@app.route('/prototip/children', methods=['GET'])
def get_children():
    return jsonify(children)

@app.route('/prototip/children/<int:id>', methods=['GET'])
def get_child_by_id(id):
    child = next((c for c in children if c['id'] == id), None)
    return jsonify(child) if child else (jsonify({"error": "Child not found"}), 404)

@app.route('/prototip/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    
    if user:
        return jsonify({"id": user['id'], "username": user['username'], "email": user['email'], "role": user['role']}), 200
    
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/prototip/getchildren/<username>', methods=['GET'])
def get_children_by_user(username):
    user = next((u for u in users if u['username'] == username), None)
    if user:
        children_ids = [rel['child_id'] for rel in relation_user_child if rel['user_id'] == user['id']]
        user_children = [child for child in children if child['id'] in children_ids]
        return jsonify(user_children)
    else:
        return jsonify({"error": "User not found"}), 404

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)

