


import pymongo 


def MongoDB(database, host, port=27017):
    myclient = pymongo.MongoClient(f"mongodb://{host}:{port}/")
    db_object = myclient[database]
    return db_object
