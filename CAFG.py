import mysql.connector
import EventHandler

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="surviver",
        password="123",
        database="flight_game",
        charset="latin1",
        collation="latin1_swedish_ci",
    )
    print("Connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM airport")
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")


print("___________________________________________________________________________")
print("Suddenly and without warning your spaceship explodes.")
print("You find yourself as a stranger in a strange land.")
print("You deside to become a tourist as there is nothing else to do.")
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print()
EventHandler.turnhandler()
