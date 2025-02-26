import mysql.connector

# Connect to MariaDB
conn = mysql.connector.connect(
    host="localhost", user="surviver", password="123", database="flight_game"
)
cursor = conn.cursor()

cursor.execute("SELECT * from airport;")
