from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

client =  MongoClient()
db = client.labflask
celebrities = db.celebrities
movies = db.movies

app = Flask("CelebritiesAPI")
#app.config["DEBUG"] = True # Esto es lo mismo que app.run(debug=True)

#With this I create the basis of the API
@app.route('/', methods=['GET'])
def home():
    return "Welcome! This site is a prototype API for celebrities information" #Se mostrará este mensaje cuando arrancas la API


def insert_celebrity(name, occupation, phrase):
    celebrity_data = {"name": f'{name}',
                      "occupation": f'{occupation}', 
                      'phrase': f'{phrase}'}
    cel_info =  celebrities.insert_one(celebrity_data)
    return cel_info.inserted_id


##FUNCIONES A LAS QUE LLAMARÉ MÁS ADELANTE:
def details(id):
    return list(db.celebrities.find({"_id": ObjectId(id)}, {"_id": 0}))




##ENDPOINTS##


#Get celebrities 
@app.route("/celebrities")
def celebr ():
    info = list(db.celebrities.find({}, {"name":1, "_id":0}))
    return dumps(info)


#Get details celebrity:
@app.route("/celebrities/details/<id>")
def celebrity_details(id):
    id = str(id)

    try:
        det = details(id)

        return dumps(det)

    except:
        return "Sorry, something was wrong"

#Create new entry
@app.route("/celebrities/new/<name>/<occupation>/<phrase>")
def new_entry(name, occupation, phrase):
    insert_celebrity(name, occupation, phrase)
    return "Ok! The new celebrity was added"

#Remove an entry
@app.route("/celebrities/")
def remove(id):
    pass


app.run(debug=True)