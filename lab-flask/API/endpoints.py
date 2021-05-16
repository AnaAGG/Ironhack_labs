from api import app
from pymongo import MongoClient

client =  MongoClient()
db = client.labflask
celebrities = db.create_collection(name = 'celebrities')
movies = db.create_collection(name= 'movies')

@app.route("/celebrities/insert", methods=['POST'])
def insert_celebrity(**celebrity):
    actors =  celebrities.insert_one(celebrity)
    return actors.inserted_id
