from helpers.mongoConnection import *

def check_params(kwargs, obligatory, at_least_one=None):
    for param in obligatory:
        if param not in kwargs.keys():
            return False
    if at_least_one:
        contains = 0
        for param in at_least_one:
            if param in kwargs.keys():
                contains +=1
        if contains == 0:
            return False
    return True 

def check_exists(query,collection):
    res = read_coll(collection,query)
    if len(res) > 0:
        return True
    else:
        return False