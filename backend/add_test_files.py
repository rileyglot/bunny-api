import sqlite3

connection = sqlite3.connect("bunnies.db")
cursor = connection.cursor()
cursor.execute("INSERT INTO Bunnies (Filename, Breed) VALUES ('bunny1.png', 'Netherland Dwarf'), ('bunny2.png', 'Unknown'), ('bowl-bunny.png', 'Mini Lop');")
connection.commit()
connection.close()

# Add test images to db