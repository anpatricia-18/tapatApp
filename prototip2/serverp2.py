import dadesServer as dades
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dades d'exemple
children = [{"id": 1, "name": "Child 1"}, {"id": 2, "name": "Child 2"}]
tap = [{"id": 1, "name": "Tap 1"}, {"id": 2, "name": "Tap 2"}]
roles = [{"id": 1, "name": "Role 1"}, {"id": 2, "name": "Role 2"}]
status = [{"id": 1, "name": "Status 1"}, {"id": 2, "name": "Status 2"}]
treatment = [{"id": 1, "name": "Treatment 1"}, {"id": 2, "name": "Treatment 2"}]
relation_user_child = [{"user_id": 1, "child_id": 1}]

# Endpoints per a cada entitat

# Children
@app.route('/child', methods=['GET'])
def get_child():
    return jsonify(children)

@app.route('/child/<int:id>', methods=['GET'])
def get_child_by_id(id):
    child = next((c for c in children if c['id'] == id), None)
    if child:
        return jsonify(child)
    return jsonify({"error": "Child not found"}), 404

# Taps
@app.route('/tap', methods=['GET'])
def get_tap():
    return jsonify(tap)

@app.route('/tap/<int:id>', methods=['GET'])
def get_tap_by_id(id):
    tap_data = next((t for t in tap if t['id'] == id), None)
    if tap_data:
        return jsonify(tap_data)
    return jsonify({"error": "Tap not found"}), 404

# Roles
@app.route('/roles', methods=['GET'])
def get_roles():
    return jsonify(roles)

@app.route('/role/<int:id>', methods=['GET'])
def get_role_by_id(id):
    role = next((r for r in roles if r['id'] == id), None)
    if role:
        return jsonify(role)
    return jsonify({"error": "Role not found"}), 404

# Statuses
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(status)

@app.route('/status/<int:id>', methods=['GET'])
def get_status_by_id(id):
    status_data = next((s for s in status if s['id'] == id), None)
    if status_data:
        return jsonify(status_data)
    return jsonify({"error": "Status not found"}), 404

# Treatments
@app.route('/treatment', methods=['GET'])
def get_treatment():
    return jsonify(treatment)

@app.route('/treatment/<int:id>', methods=['GET'])
def get_treatment_by_id(id):
    treatment_data = next((t for t in treatment if t['id'] == id), None)
    if treatment_data:
        return jsonify(treatment_data)
    return jsonify({"error": "Treatment not found"}), 404

# Relació User-Child
@app.route('/relation_user_child', methods=['GET'])
def get_relation_user_child():
    return jsonify(relation_user_child)

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)