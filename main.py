from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from services.question_paper import QuestionPaperServices
from flask_mongoengine import MongoEngine
from services.user import UserServices
#from requests import request
from config.parsers import classname_post_args

app = Flask(__name__)

database_name = "sakec_cet_db"
DB_URI = "mongodb+srv://sakeccet:sakeccet@sakec-cet.zufjepd.mongodb.net/?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)
api = Api(app)

# classname_post_args = reqparse.RequestParser()
# classname_post_args.add_argument("name", type=str, help="Name of the exam is required", required=True)
# classname_post_args.add_argument("type", type=str, help="Type of the exam")
# classname_post_args.add_argument("year", type=int, help="Year of the exam")

names = {"cet": {"type": "offline", "year": 2022}, 
         "jee": {"type": "onlTESTING HEHEine", "year": 2023}}

def abort_if_name_doesnt_exist(name):
    if name not in names:
        abort(404, message = "Could not find name, try again...")

class HelloWorld(Resource):
    def get(self, name):
        abort_if_name_doesnt_exist(name)
        return names[name]

    def post(self, name):
        if name in names:
            abort(409, message = "Name already exists")
        args = classname_post_args.parse_args()
        names[name] = args
        return args, 202

    def put(self, name):
        args = classname_post_args.parse_args()
        names[name] = args
        return names[name], 201

    def delete(self, name):
        abort_if_name_doesnt_exist(name)
        del names[name]
        return '', 204


api.add_resource(HelloWorld, "/helloworld/<string:name>")

api.add_resource(UserServices, "/users")
#api.add_resource(ParticularUserServices, "/users/<string:userid>")
api.add_resource(QuestionPaperServices, "/users/<string:userid>/questionpapers")
#api.add_resource(ResultServices, "/users/<string:userid>/questionpapers/results")
#api.add_resource(ParticularQuestionPaperServices, "/users/<string:userid>/questionpapers/<string:questionpaperid>")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
