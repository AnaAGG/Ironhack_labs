from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId

def insert_celebrity(obj):
    if not check_params(obj,["name","occupation"]):
        return {"response":400,"message":"Bad Request: 'name' and 'occupation' are obligatory parameters"}
    q = {"name":obj["name"]}
    if check_exists(q,"celebrities"):
        return {"response":400,"message":"Bad Request: there is already a celebrity with that name"}
    res = write_coll("celebrities",obj)
    return res.inserted_id

def list_celebrities():
    res = read_coll("celebrities",{})
    response = {c["name"]:str(c["_id"]) for c in res}
    return response

def get_celebrity(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"celebrities"):
        return {"response":400,"message":"Bad Request: celebrity with given id does not exist"}
    return read_coll("celebrities",q)

def delete_celebrity(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"celebrities"):
        return {"response":400,"message":"Bad Request: celebrity with given id does not exist"}
    delete_coll("celebrities",q)
    return {"response":200,"message":"Celebrity successfully deleted"}

def update_celebrity(obj):
    if not check_params(obj,["id"],["name","occupation","catch_phrase"]):
        return {"response":400,"message":"Bad Request: 'id' and at least one of ['name','occupation','catch_phrase'] are obligatory parameters"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"celebrities"):
        return {"response":400,"message":"Bad Request: celebrity with given id does not exist"}
    obj.pop("id")
    update_coll("celebrities",q,obj)
    return {"response":200,"message":"Celebrity successfully updated"}

def get_works(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"celebrities"):
        return {"response":400,"message":"Bad Request: celebrity with given id does not exist"}
    cel = list(read_coll("celebrities",q))[0]
    query = {"cast":q["_id"]}
    res = read_coll("movies",query)
    return {"name":cel["name"],"works":[movie["title"] for movie in res]}