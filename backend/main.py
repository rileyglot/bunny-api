from fastapi import FastAPI
import sqlite3
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

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
    image_url = "http://127.0.0.1:8000/static/bunny-imgs/" + value[1]
    return {
        "id": value[0],
        "filename": value[1],
        "breed": value[2],
        "image_url": image_url
            }