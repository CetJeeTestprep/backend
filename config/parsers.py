from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

classname_post_args = reqparse.RequestParser()
classname_post_args.add_argument("name", type=str, help="Name of the exam is required", required=True)
classname_post_args.add_argument("type", type=str, help="Type of the exam")
classname_post_args.add_argument("year", type=int, help="Year of the exam")