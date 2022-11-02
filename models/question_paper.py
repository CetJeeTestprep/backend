from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
#from requests import request

class QuestionPaperServices(Resource):

    user_post_args = reqparse.RequestParser()

    def __init__(self) -> None:
        user_post_args = reqparse.RequestParser()
        user_post_args.add_argument("name", type=str, help="Name of the exam is required", required=True)
        user_post_args.add_argument("type", type=str, help="Type of the exam")
        super().__init__()

    def get(self, name):
        return name, 200

    def post(self, name):
        return name, 202

    def put(self, name):
        return name, 201

    def delete(self, name):
        return '', 204