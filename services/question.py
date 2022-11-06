from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from schema.mongo_model.mongo_question_paper import MongoQuestionPaperModel
#from requests import request

class QuestionServices(Resource):

    def __init__(self) -> None:
        super().__init__()

    def get(self, name):
        return name, 200

    def post(self, name):
        return name, 202

    def put(self, name):
        return name, 201

    def delete(self, name):
        return '', 204