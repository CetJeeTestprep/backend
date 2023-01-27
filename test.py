# import requests

# BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "helloworld/ct")
# #input()
# #response = requests.post(BASE + "helloworld/gre", {"name": "gre", "year":10})

# print(response.json())
import pandas as pd
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

# user_questions_doc = MongoUserQuestionsModel.objects()
# print("check:",user_questions_doc[0].userId)

# question_dataset = pd.read_csv('../datasets/matrices_question.csv')
# print("DATA:",question_dataset.columns)

# user = MongoUserModel.objects(id='ba9bdb80-5dbb-11ed-83ee-646c802a23ae')
# print("USER COLLECTION:",user[0].attemptedQuestionPapers==None)
# print(type(user[0].to_json()))

j = [
    {
        "question_paper_id": "614d0098-5f77-11ed-bed1-646c802a23ae",
        "score": 100,
        "difficulty": 2
    },
    {
        "question_paper_id": "1631835c-5f4b-11ed-b40b-646c802a23ae",
        "score": 56,
        "difficulty": 3
    },
    {
        "question_paper_id": "5ca4f2de-5f77-11ed-8558-646c802a23ae",
        "score": 100,
        "difficulty": 1
    }
]

sj = str(j)

def convertStringToListOfDict(sj):
    length = len(sj)
    sjNoL = sj[2:length-2]
    print(sjNoL)
    dictStrings = sjNoL.split(',')
    dictList = []
    for s in dictStrings:
        print(s)
        d = {}
        sClean = s
        print(sClean)
        keyValList = sClean.split(',')
        print(keyValList)
        
        for i in range(len(keyValList)):
            kv = keyValList[i].split(': ')
            key = kv[0][1:len(kv[0])-1]
            value = kv[1][1:len(kv[1])-1]
            print("KEY:",key)
            print("VALUE:",value)
            d[key] = value
            print("-----------------------------------------------------")
            print(d)
            print("-----------------------------------------------------")

        dictList.append(d)
        print(dictList)
        print("______________________________________________________")
    return dictList

convertStringToListOfDict(sj)
