from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId

def insert_movie(obj):
    if not check_params(obj,["title","year","genre"]):
        return {"response":400,"message":"Bad Request: 'title', 'year' and 'genre' are obligatory parameters"}
    q = {"title":obj["title"]}
    if check_exists(q,"movies"):
        return {"response":400,"message":"Bad Request: there is already a movie with that name"}
    res = write_coll("movies",obj)
    return res.inserted_id

def list_movies():
    res = read_coll("movies",{})
    response = {c["title"]:str(c["_id"]) for c in res}
    return response

def get_movie(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"movies"):
        return {"response":400,"message":"Bad Request: movie with given id does not exist"}
    return read_coll("movies",q)

def delete_movie(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"movies"):
        return {"response":400,"message":"Bad Request: movie with given id does not exist"}
    delete_coll("movies",q)
    return {"response":200,"message":"movie successfully deleted"}

def update_movie(obj):
    if not check_params(obj,["id"],["title","year","genre","plot"]):
        return {"response":400,"message":"Bad Request: 'id' and at least one of ['title','year','genre','plot'] are obligatory parameters"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"movies"):
        return {"response":400,"message":"Bad Request: movie with given id does not exist"}
    obj.pop("id")
    update_coll("movies",q,obj)
    return {"response":200,"message":"movie successfully updated"}

def add_cast(obj):
    if not check_params(obj,["movie_id","celebrity_id"]):
        return {"response":400,"message":"Bad Request: 'movie_id' and 'celebrity_id' are obligatory parameters"}
    movie = {"_id":ObjectId(obj["movie_id"])}
    if not check_exists(movie,"movies"):
        return {"response":400,"message":"Bad Request: movie with given id does not exist"}
    celebrity = {"_id":ObjectId(obj["celebrity_id"])}
    if not check_exists(celebrity,"celebrities"):
        return {"response":400,"message":"Bad Request: celebrity with given id does not exist"}
    push_coll("movies",movie,{"cast":celebrity["_id"]})
    return {"response":200,"message":"movie cast successfully updated"}
