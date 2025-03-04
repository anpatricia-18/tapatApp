import requests

BASE_URL = "http://192.168.144.160:10050"

class User:
    def __init__(self, id, username, email, role):
        self.id = id
        self.username = username
        self.email = email
        self.role = role  # Afegit l'atribut 'role' per poder diferenciar els rols.

    def __str__(self):
        return f"[Usuari] ID: {self.id}, Username: {self.username}, Email: {self.email}, Rol: {self.role}"


class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"[Infant] ID: {self.id}, Nom: {self.name}, Promig son: {self.sleep_average}, Tractament: {self.treatment}, Temps: {self.time}h"


class APIClient:
    BASE_URL = "http://localhost:5000/prototip"  # Port on s'executa el servidor

    @staticmethod
    def login(username, password):
        try:
            response = requests.post(f"{APIClient.BASE_URL}/login", json={"username": username, "password": password})
            if response.status_code == 200:
                data = response.json()
                # Es retorna l'usuari amb el seu rol (cuidador, infant, metge)
                return User(data['id'], data['username'], data['email'], data['role'])
            else:
                print(f"Error: {response.json().get('error', 'Credencials incorrectes')}")
                return None
        except Exception as e:
            print(f"Error de connexió: {e}")
            return None

    @staticmethod
    def get_children(username):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/getchildren/{username}")
            if response.status_code == 200:
                children_data = response.json()
                return [Child(c["id"], c["name"], c["sleep_average"], c["treatment"], c["time"]) for c in children_data]
            else:
                print(f"Error: {response.json().get('error', 'No s\'han trobat infants')}")
                return []
        except Exception as e:
            print(f"Error de connexió: {e}")
            return []


class ConsoleView:
    @staticmethod
    def menu():
        print("\n--- MENÚ ---")
        print("1. Iniciar sessió")
        print("2. Consultar nens associats")
        print("3. Sortir")

    @staticmethod
    def run():
        logged_in_user = None

        while True:
            if logged_in_user is None:
                # Si no hem iniciat sessió, mostrem el menú de login
                username = input("Introdueix el teu nom d'usuari: ")
                password = input("Introdueix la teva contrasenya: ")
                logged_in_user = APIClient.login(username, password)

                if logged_in_user:
                    print(f"Benvingut {logged_in_user.username} ({logged_in_user.role})")
                else:
                    print("Error en iniciar sessió, intenta-ho de nou.")
                    continue
            else:
                # Si ja estem loguejats, mostrem el menú segons el rol
                ConsoleView.menu()
                option = input("Selecciona una opció: ")

                if option == "1":
                    # Aquest menú es desactiva quan estem loguejats, només es pot consultar
                    print("Ja estàs loguejat.")
                elif option == "2" and logged_in_user.role == "cuidador":
                    # Si el rol és 'cuidador', mostrem els nens associats
                    children = APIClient.get_children(logged_in_user.username)
                    if children:
                        for child in children:
                            print(child)
                    else:
                        print("Aquest usuari no té nens associats.")
                elif option == "2" and logged_in_user.role == "metge":
                    print("Accés a consulta mèdica no disponible en aquest menú.")
                elif option == "3":
                    print("Fins aviat!")
                    break
                else:
                    print("Opció incorrecta. Si us plau, intenta-ho de nou.")


if __name__ == "__main__":
    ConsoleView.run()