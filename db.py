import mysql.connector
from config import DB_CONFIG

class Database: 
    def connect(self):
        return mysql.connector.connect(**DB_CONFIG)
    
    def register_user(self, name, username, password):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
            conn.commit()
            return True
        except:
            return False
        finally:
            conn.close()

    def login_user(self, username, password):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            return user
        except:
            return None
        finally:
            conn.close() 
    
    def fetch_questions(self):
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM questions")
            questions = cursor.fetchall()
            return questions
        except Exception as e:
            print("Error Fetching Questions:", e)
            return []
        finally:
            conn.close()