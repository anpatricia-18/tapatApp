import mysql.connector

def list_all_users():
    try:
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )

        cursor = connection.cursor()
        # Consulta para obtener todos los registros de la tabla users
        query = "SELECT * FROM users"
        cursor.execute(query)

        # Recuperar y mostrar los resultados
        users = cursor.fetchall()
        for user in users:
            print(user)

    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    list_all_users()