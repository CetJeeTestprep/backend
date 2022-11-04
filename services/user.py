from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import requests
from schema.user import UserModel
import constants.urls as urls
#from requests import request

BASE = urls.BASE
class UserServices(Resource):

    user_post_args = reqparse.RequestParser()

    def __init__(self, user:UserModel) -> None:
        user_post_args = reqparse.RequestParser()
        user_post_args.add_argument("user", type=UserModel, help="User is required", required=True)
        super().__init__()

    def get(self, user:UserModel):
        response = requests.get(BASE + "users/" + user.id)
        return user, 200

    def post(self, user:UserModel):
        return user, 202

    def put(self, user:UserModel):
        return user, 201

    def delete(self, user:UserModel):
        return '', 204

class ParticularUserServices(Resource):

    user_post_args = reqparse.RequestParser()

    def __init__(self, user:UserModel) -> None:
        user_post_args = reqparse.RequestParser()
        user_post_args.add_argument("user", type=UserModel, help="User is required", required=True)
        super().__init__()

    def get(self, user:UserModel):
        response = requests.get(BASE + "users/" + user.id)
        return user, 200

    def post(self, user:UserModel):
        return user, 202

    def put(self, user:UserModel):
        return user, 201

    def delete(self, user:UserModel):
        return '', 204