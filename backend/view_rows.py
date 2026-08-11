import sqlite3

connection = sqlite3.connect("bunnies.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM Bunnies")
values = cursor.fetchall()

for item in values:
    print(item)

connection.close()