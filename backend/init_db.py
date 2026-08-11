import sqlite3

connection = sqlite3.connect("bunnies.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Bunnies (id INTEGER PRIMARY KEY AUTOINCREMENT, Filename VARCHAR(255) UNIQUE NOT NULL, Breed VARCHAR(30) NOT NULL);")
connection.commit()
connection.close()


# Make bunnies.db