from flask import Flask , request
from flask_restful import Resource, Api
import uuid
import configparser
config = configparser.ConfigParser()
config.read('../config.ini')

app=Flask(__name__)
api=Api(app)


items=[]
subscription_list = []
subscription_version = []
print(config.sections())
class Datasource(Resource):
    def get(self, data):
        for item in items:
            if item["key"] == data:
                return item, 200
        return {"key" : None}, 404


    def post(self, data):
        if data == "insert":
            body_data = request.get_json(force=True)
            item = next(filter(lambda x: x["key"] == body_data["key"], items ), None)
            if item is None:
                item = {"key":body_data["key"],"value":body_data["value"]}
                items.append(item)
                return item , 201
            else:
                return {"message": "set command can set unique key and values "+body_data["key"]+" already exists"}
        return {"message" : "invalid path"}


    def delete(self, data):
        for i in range(len(items)):
            if items[i]['key'] == data:
                del items[i]
                if data in subscription_list:
                    subscription_list.remove(data)
                break
        return {"status":"success"}, 200

    def put(self,data):
        body_data = request.get_json(force=True)
        item = next(filter(lambda x: x["key"] == body_data["key"], items ), None)
        print(item)
        print(body_data)
        if item is None:
            items.append(body_data)
            return body_data , 201
        else:
            if body_data["key"] in subscription_list:
                oldvalue=item["value"]
                item.update(body_data)
                subscription_list.remove(body_data["key"])
                return {"message":"subscription key "+body_data["key"]+" has been updated", "key":body_data["key"],"oldvalue":oldvalue,"newvalue":body_data["value"]}
            else:
                item.update(body_data)
                return body_data , 200

class Subscribe(Resource):
    def post(self, data):
        subscription_data = data
        for item in items:
            if item["key"] == data:
                subscription_list.append(data)
                return {"item":data,"message": data+" has been Successfully added to subscription list", "status": 200}
        return {"message" : "not found", "status": 404}


    def get(self, data):
        if data == "list":
            return {"subscription_list": subscription_list} ,200
class Alllist(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Datasource,"/key/<string:data>")
api.add_resource(Alllist,"/alllist")
api.add_resource(Subscribe,"/subscribe/<string:data>")

app.run(host='0.0.0.0',port=5000)
