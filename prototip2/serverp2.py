from flask import Flask, jsonify, request

app = Flask(__name__)

# Dade d'exemple
children = [
    {"id": 1, "name": "Child 1"},
    {"id": 2, "name": "Child 2"}
]

taps = [
    {"id": 1, "name": "Tap 1"},
    {"id": 2, "name": "Tap 2"}
]

roles = [
    {"id": 1, "name": "Role 1"},
    {"id": 2, "name": "Role 2"}
]

statuses = [
    {"id": 1, "name": "Status 1"},
    {"id": 2, "name": "Status 2"}
]

treatments = [
    {"id": 1, "name": "Treatment 1"},
    {"id": 2, "name": "Treatment 2"}
]

relation_user_child = [
    {"user_id": 1, "child_id": 1}
]

# Endpoints para cada entidad
@app.route('/children', methods=['GET'])
def get_children():
    return jsonify(children)

@app.route('/children/<int:id>', methods=['GET'])
def get_child_by_id(id):
    child = next((c for c in children if c['id'] == id), None)
    return jsonify(child) if child else (jsonify({"error": "Child not found"}), 404)

@app.route('/taps', methods=['GET'])
def get_taps():
    return jsonify(taps)

@app.route('/taps/<int:id>', methods=['GET'])
def get_tap_by_id(id):
    tap = next((t for t in taps if t['id'] == id), None)
    return jsonify(tap) if tap else (jsonify({"error": "Tap not found"}), 404)

@app.route('/roles', methods=['GET'])
def get_roles():
    return jsonify(roles)

@app.route('/roles/<int:id>', methods=['GET'])
def get_role_by_id(id):
    role = next((r for r in roles if r['id'] == id), None)
    return jsonify(role) if role else (jsonify({"error": "Role not found"}), 404)

@app.route('/statuses', methods=['GET'])
def get_statuses():
    return jsonify(statuses)

@app.route('/statuses/<int:id>', methods=['GET'])
def get_status_by_id(id):
    status = next((s for s in statuses if s['id'] == id), None)
    return jsonify(status) if status else (jsonify({"error": "Status not found"}), 404)

@app.route('/treatments', methods=['GET'])
def get_treatments():
    return jsonify(treatments)

@app.route('/treatments/<int:id>', methods=['GET'])
def get_treatment_by_id(id):
    treatment = next((t for t in treatments if t['id'] == id), None)
    return jsonify(treatment) if treatment else (jsonify({"error": "Treatment not found"}), 404)

@app.route('/relation_user_child', methods=['GET'])
def get_relation_user_child():
    return jsonify(relation_user_child)

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True) #192.168.144.160,  host:"0.0.0.0",  port=10050
