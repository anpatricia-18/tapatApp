import mysql.connector
from mysql.connector import Error

def list_all_users():
    try:
        # Intentar conectar
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatapp"
        )

        if connection.is_connected():
            print("✅ Conexión exitosa a la base de datos.")
            cursor = connection.cursor(dictionary=True)

            # Consulta
            query = "SELECT * FROM user"
            cursor.execute(query)
            users = cursor.fetchall()

            # Mostrar usuarios
            if users:
                for user in users:
                    print(user)
            else:
                print("⚠️ No hay usuarios en la base de datos.")

            cursor.close()
        else:
            print("❌ No se pudo establecer la conexión con la base de datos.")

    except Error as e:
        print(f"❌ Error al conectar o consultar la base de datos: {e}")

    finally:
        # Cierre de conexión
        if connection.is_connected():
            connection.close()
            print("🔒 Conexión cerrada correctamente.")

if __name__ == "__main__":
    list_all_users()

