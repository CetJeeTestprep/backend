from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import requests
from schema.user import UserModel
from config.parsers import user_services_post_args
import constants.urls as urls
from flask_mongoengine import MongoEngine
from schema.mongo_model.mongo_user import MongoUserModel
#from requests import request

BASE = urls.BASE
class UserServices(Resource):

    def __init__(self) -> None:
        super().__init__()

    #get all users
    def get(self):
        #response = requests.get(BASE + "users/" + user.id)
        print("FETCHING ALL USERS")
        user = MongoUserModel.objects()
        # if(len(user)==0):
        #     abort(404, message="No existing users")
        return user.to_json(), 200

    #login
    def post(self):
        args = user_services_post_args.parse_args()
        user_doc = MongoUserModel.objects(email=args['email'])
        if(len(user_doc)==0):
            abort(404, message="This user does not exist. Signup to create a new account.")
        if(user_doc[0]['password']!=args['password']):
            return {'message':"Invalid password, try again."}
        return user_doc[0].to_json(), 202

    def put(self):
        args = user_services_post_args.parse_args()

        user_doc = MongoUserModel.objects(email=args['email'])
        if(len(user_doc)!=0):
            abort(409, message="This user already exists.")

        user = MongoUserModel(id='22')
        user.name = args['name']
        user.email = args['email']
        user.password = args['password']
        user.phone = args['phone']
        # user.userType = args['user_type']
        # user.attemptedQuestionPapers = args['attempted_question_papers']
        user.save()
        return {
            'message': 'Signup successful!'
        }, 201

    def delete(self):
        return '', 204

class ParticularUserServices(Resource):

    def __init__(self) -> None:
        super().__init__()

    #get user details
    def get(self, user_id):
        user_doc = MongoUserModel.objects(id=user_id)
        if(len(user_doc)==0):
            abort(404, message="This user id does not exist.")
        return user_doc[0].to_json(), 200

    #login
    def post(self):
        args = user_services_post_args.parse_args()
        user_doc = MongoUserModel.objects(email=args['email'])
        if(len(user_doc)==0):
            abort(404, message="This user does not exist. Signup to create a new account.")
        if(user_doc[0]['password']!=args['password']):
            return "Invalid password, try again."
        return user_doc[0].to_json(), 202

    #signup
    def put(self):
        args = user_services_post_args.parse_args()

        user_doc = MongoUserModel.objects(email=args['email'])
        if(len(user_doc)!=0):
            abort(409, message="This user already exists.")

        user = MongoUserModel()
        user.name = args['name']
        user.email = args['email']
        user.password = args['password']
        user.phone = args['phone']
        user.userType = args['user_type']
        user.attemptedQuestionPapers = args['attempted_question_papers']
        user.save()
        return user, 201

    def delete(self):
        return '', 204