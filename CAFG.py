import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="surviver",
    password="123",
    database="flight_game",
)
cursor = conn.cursor()

# Read and execute the SQL file
with open("flight_game.sql", "r") as file:
    sql_script = file.read()
    for statement in sql_script.split(";"):  # Split by statements
        if statement.strip():  # Ignore empty statements
            cursor.execute(statement)

conn.commit()
conn.close()

print("SQL file executed successfully.")

