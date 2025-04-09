import mysql.connector

class daoUser:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            database="tapatapp",
            user="root",
            password="root"
        )
        self.cursor = self.connection.cursor()

    def create_user(self, username, email, password):
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def update_user(self, user_id, username=None, email=None, password=None):
        query = "UPDATE users SET "
        updates = []
        values = []

        if username:
            updates.append("username = %s")
            values.append(username)
        if email:
            updates.append("email = %s")
            values.append(email)
        if password:
            updates.append("password = %s")
            values.append(password)

        query += ", ".join(updates) + " WHERE id = %s"
        values.append(user_id)
        self.cursor.execute(query, tuple(values))
        self.connection.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()