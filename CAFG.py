import mysql.connector

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
