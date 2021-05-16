#To create a connection with mongo and create BBDD and collections
from pymongo import MongoClient

client =  MongoClient()
db = client.labflask
celebrities = db.create_collection(name = 'celebrities')
movies = db.create_collection(name= 'movies')

def insert_actor(**actor):
    actors =  celebrities.insert_one(actor)
    return actors.inserted_id


def insert_movies(**movie):
    moviess = movies.insert_one(**movie)
    return moviess.inserted_id
