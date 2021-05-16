from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

client =  MongoClient()
db = client.labflask
celebrities = db.celebrities
movies = db.movies


def insert_celebrity(name, occupation, phrase):
    celebrity_data = {"name": f'{name}',
                      "occupation": f'{occupation}', 
                      'phrase': f'{phrase}'}
    cel_info =  celebrities.insert_one(celebrity_data)
    return cel_info.inserted_id

insert_celebrity('Brad Pitt', 'actor', 'Debes perder todo para ganar algo.')
insert_celebrity('Benedict Cumberbatch', 'actor', " Debes perder todo para ganar algo.")
insert_celebrity('Scarlett Johansson', 'actor', " Si voy a hacer algo tengo que ser muy buena en ello, o mejor no lo hago.")