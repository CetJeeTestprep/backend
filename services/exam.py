from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import requests
import constants.urls as urls
#from requests import request

BASE = urls.BASE
class ExamServices(Resource):

    user_post_args = reqparse.RequestParser()

    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return 200

    def post(self):
        return 202

    def put(self):
        return 201

    def delete(self):
        return '', 204