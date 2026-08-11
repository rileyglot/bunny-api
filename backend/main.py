from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def test():
    return {"message":"hello"}

@app.get("/api/bunnies/random")
def get_random_bunny():
    connection = sqlite3.connect("bunnies.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Bunnies ORDER BY RANDOM() LIMIT 1;")
    value = cursor.fetchone()
    connection.close()
    return {
        "id": value[0],
        "filename": value[1],
        "breed": value[2]
            }