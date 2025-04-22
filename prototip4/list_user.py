import mysql.connector

def list_all_users():
    connection = None
    cursor = None
    try:
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM user"
            cursor.execute(query)

            users = cursor.fetchall()
            for user in users:
                print(user)
        else:
            print("No se pudo establecer la conexión con la base de datos.")

    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

if __name__ == "__main__":
    list_all_users()
