# import requests

# BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "helloworld/ct")
# #input()
# #response = requests.post(BASE + "helloworld/gre", {"name": "gre", "year":10})

# print(response.json())

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from services.question_paper import QuestionPaperServices
from flask_mongoengine import MongoEngine
from services.user import UserServices
from schema.mongo_model.mongo_user import MongoUserModel
from schema.mongo_model.mongo_question_paper import MongoQuestionPaperModel
from schema.mongo_model.mongo_users_questions import MongoUserQuestionsModel
#from requests import request
import datetime
from config.parsers import classname_post_args

app = Flask(__name__)

database_name = "test"
DB_URI = "mongodb+srv://sakeccettestprep:password_123@sakeccet.c0u0ayv.mongodb.net/?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)
api = Api(app)

# user = MongoUserModel(id='10')
# user.name = 'Test all'
# user.email = 'kashishmaru2001@gmail.com'
# user.password = '123456'
# user.save()
#
# questions = MongoQuestionPaperModel(id='1')
# questions.exam = 'CET'
# questions.marksPerQuestion = 2
# questions.date = datetime.datetime.now()
# questions.difficulty = 2
# questions.type = 'subject'
# questions.maxAttempts = -1
# questions.totalMarks = 40
# questions.duration = 20
# questions.questions = []
# questions.save()
#
# user_question = MongoUserQuestionsModel(id='0-0')
# user_question.userId = '0'
# user_question.questionId = '0'
# user_question.save()

# user = MongoUserModel.objects(email='kashishmaru2001@gmail.com')
# print("USER COLLECTION:",user[0].to_json())
# print(type(user[0].to_json()))