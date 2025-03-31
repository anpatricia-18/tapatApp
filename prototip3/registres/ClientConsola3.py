#Aquest client de consola recull dades d'entrada de l'usuari i les envia al servidor
# per a que les processi pel seu username. El servidor respon amb un missatge que el client mostra a la consola.

import requests

#classe usuari amb els seus atributs 
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Email: {self.email}"

#la classe Child amb els seus atributs
class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment  
        self.time = time

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Sleep Average: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}"
    
#classe APIClient 
BASE_URl = "http://localhost:5000/prototip3" #port per defecte 
token  = None #per guardar el token d'autenticació

@staticmethod
def login(username, password):
    try:
        response = requests.post(f"{APIClient.BASE_URL}/login", json={"username": username, "password": password})
        if response.status_code == 200:
                data = response.json()
                APIClient.token = data["token"]  # Guardem el token per a futures peticions
                print("El login no està ben fet!")
                return User(data['id'], data['username'], data['email']) 
        else:
                print(f"Error: {response.json().get('error', 'Usuari o contrasenya incorrectes')}")
                return None
    except Exception as ex:
        print(f"Connection Error: {ex}")
        return None
    
@staticmethod
def get_user(username):
    if not APIClient.token:
        print("No hi ha cap usuari autenticat.")
        return None
        
    try:    
         headers = {"Authorization": APIClient.token}
         response = requests.get(f"{APIClient.BASE_URL}/getuser", headers=headers)
         if response.status_code == 200:
                data = response.json()
                return User(data['id'], data['username'], data['email'])
         else:
                print(f"Error: {response.json().get('error', 'No es pot obtenir l'usuari')}")
                return None

    except Exception as ex:
        print(f"Connection Error: {ex}")
        return None

@staticmethod
def get_children(username):
    try:    
         response = requests.get(f"{APIClient.BASE_URL}/getchildren/{username}")
         if response.status_code == 200:
                children_data = response.json()
                return [Child(child['id'], child['name'], child['sleep_average'], child['treatment'], child['time']) for child in children_data]
         else:
                print(f"Error: {response.json().get('error', 'No es poden obtenir als nens')}")
                return None

    except Exception as ex:
        print(f"Connection Error: {ex}")
        return []

#creem la classe ConsoleView per a gestionar la interacció amb l'usuari
class ConsoleView:
logged_user = None

@staticmethod
def login():
 username = input("Introdueix el teu nom d'usuari: ")
password = input("Introdueix la teva contrasenya: ")  
ConsoleView.logged_user = APIClient.login(username, password)

@staticmethod
def Menu():
    print("1. Menu")
    print("2. Consultar informació del user")
    print("3. Consultar informació dels nens del user")
    print("4. Bye Bye!")

@staticmethod
def run():
print("Benvingut a l'aplicació TapatApp!")
ConsoleView.login()
 if ConsoleView.logged_user:
    while True:
        ConsoleView.Menu()
        option = input("Introdueix una opció: ")
        if option == "1":
        print(ConsoleView.logged_user)
        elif option == "2":
            children = APIClient.get_children(ConsoleView.logged_user.username)
            if children:
                for child in children:
                    print(child)
        elif option == "3":
            print("Bye Bye!")
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

    if __name__ == "__main__":
        ConsoleView.run()
        
    



    
    

