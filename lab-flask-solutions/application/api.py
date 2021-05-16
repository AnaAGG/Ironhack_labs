from flask import Flask, request
from bson import json_util
from helpers.celebrities import *
from helpers.movies import *

app = Flask(__name__)

@app.route("/celebrities/new")
def  celebrities_new():
    args = dict(request.args)
    id = insert_celebrity(args)
    return json_util.dumps({"_id":id})

@app.route("/celebrities")
def celebrities():
    return json_util.dumps(list_celebrities())

@app.route("/celebrities/details")
def celebrities_details():
    args = dict(request.args)
    return json_util.dumps(get_celebrity(args))

@app.route("/celebrities/delete")
def celebrities_delete():
    args = dict(request.args)
    return json_util.dumps(delete_celebrity(args))

@app.route("/celebrities/edit")
def celebrities_edit():
    args = dict(request.args)
    return json_util.dumps(update_celebrity(args))

## Bonus

@app.route("/movies/new")
def  movies_new():
    args = dict(request.args)
    id = insert_movie(args)
    return json_util.dumps({"_id":id})

@app.route("/movies")
def movies():
    return json_util.dumps(list_movies())

@app.route("/movies/details")
def movies_details():
    args = dict(request.args)
    return json_util.dumps(get_movie(args))

@app.route("/movies/delete")
def movies_delete():
    args = dict(request.args)
    return json_util.dumps(delete_movie(args))

@app.route("/movies/edit")
def movies_edit():
    args = dict(request.args)
    return json_util.dumps(update_movie(args))

## Advanced
@app.route("/movies/cast/add")
def movies_cast_add():
    args = dict(request.args)
    return json_util.dumps(add_cast(args))

@app.route("/celebrities/works")
def celebrities_works():
    args = dict(request.args)
    return json_util.dumps(get_works(args))

app.run(debug=True)