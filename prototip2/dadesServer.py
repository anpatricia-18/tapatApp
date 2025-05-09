class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"{self.username}:{self.password}:{self.email}"

users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]
#Crear les classes Child, Tap, Role, Status i Treatment
class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]
#Classe Relació
class RelationUserChild:
    def __init__(self, user_id, child_id, rol_id):
        self.user_id = user_id
        self.child_id = child_id
        self.rol_id = rol_id

    def __str__(self):
        return f"USer: {self.user_id}, Child: {self.child_id}, Rol: {self.rol_id}

relation_user_child = [
    {"user_id": 1, "child_id": 1, "role_id": 1},
    {"user_id": 1, "child_id": 1, "role_id": 2},
    {"user_id": 2, "child_id": 2, "role_id": 1},
    {"user_id": 2, "child_id": 2, "role_id": 2}
]

class Role:  
    def __init__(self, id, type_role):
        self.id = id
        self.type_role = type_role

roles = [
    Role(id=1, type_role='Admin'),
    Role(id=2, type_role='Tutor Mare Pare'),
    Role(id=3, type_role='Cuidador'),
    Role(id=4, type_role='Seguiment')
]

class Status:  
    def __init__(self, id, name):
        self.id = id
        self.name = name

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='Percentage')
]
