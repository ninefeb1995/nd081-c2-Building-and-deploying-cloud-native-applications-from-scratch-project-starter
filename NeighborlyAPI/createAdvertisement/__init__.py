import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = 'mongodb://finalproject2databaseaccountt:Vcp62ul8ll8ddwmhdiptBhyMLTEBl4GQrYtZ4Chch1tPOMRgsYSkde5B5IVfR8hCmeKh5hJGvL9ha6YYrHuB3Q==@finalproject2databaseaccountt.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@finalproject2databaseaccountt@'  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['finalproject2database']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )