from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import requests
import constants.urls as urls
from schema.mongo_model.mongo_user import MongoUserModel

BASE = urls.BASE
class ResultServices(Resource):

    user_post_args = reqparse.RequestParser()

    def __init__(self) -> None:
        super().__init__()

    #get all results
    def get(self, user_id):
        message = "You have not attempted any tests yet."
        details = "None"
        user_doc = MongoUserModel.objects(id=user_id)
        if(len(user_doc)==0):
            abort(404, message="This user id does not exist.")
        else:
            if(user_doc[0].attemptedQuestionPapers!=None):
                message = "Results are as follows!"
                details = user_doc[0].attemptedQuestionPapers
                
        return {
            'message': message,
            'details': details
        }, 200

    #add results
    def post(self):
        return 202

    #add results
    def put(self):

        return 201

    def delete(self):
        return '', 204