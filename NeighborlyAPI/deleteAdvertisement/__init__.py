import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = 'mongodb://finalproject2databaseaccountt:Vcp62ul8ll8ddwmhdiptBhyMLTEBl4GQrYtZ4Chch1tPOMRgsYSkde5B5IVfR8hCmeKh5hJGvL9ha6YYrHuB3Q==@finalproject2databaseaccountt.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@finalproject2databaseaccountt@'  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['finalproject2database']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
