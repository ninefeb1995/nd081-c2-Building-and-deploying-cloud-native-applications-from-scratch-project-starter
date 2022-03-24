import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = 'mongodb://finalproject2databaseaccountt:Vcp62ul8ll8ddwmhdiptBhyMLTEBl4GQrYtZ4Chch1tPOMRgsYSkde5B5IVfR8hCmeKh5hJGvL9ha6YYrHuB3Q==@finalproject2databaseaccountt.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@finalproject2databaseaccountt@'  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['finalproject2database']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

