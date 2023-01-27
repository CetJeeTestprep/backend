from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from schema.mongo_model.mongo_question_paper import MongoQuestionPaperModel
from schema.mongo_model.mongo_user import MongoUserModel
from schema.mongo_model.mongo_users_questions import MongoUserQuestionsModel
import datetime
import uuid
import pandas as pd
from config.parsers import question_paper_services_post_args, particular_question_paper_services_post_args
import random
import json
#from requests import request

def convertListToJson(l):
    d = {}
    for i in range(len(l)):
        d[i] = l[i]
    return d
class QuestionPaperServices(Resource):

    def __init__(self) -> None:
        super().__init__()

    def get(self, name):
        return name, 200

    def post(self, name):
        return name, 202

    #new question paper generation
    def put(self, user_id, selected_difficulty):

        args = question_paper_services_post_args.parse_args()
        this_user_id = user_id

        # user_doc = MongoUserModel.objects(id=user_id)
        user_questions_doc = MongoUserQuestionsModel.objects()
        has_attempted_questions = False

        for i in range(len(user_questions_doc)):
            if(user_questions_doc[i].userId==this_user_id):
                has_attempted_questions = True
                break

        # question_dataset = pd.read_csv('../datasets/matrices_question.csv')
        question_dataset = pd.read_csv('https://raw.githubusercontent.com/CetJeeTestprep/backend/main/datasets/matrices_question.csv')
        print("DATA:",question_dataset.columns)
        qp_questions = []
        attempted_questions = []
        difficulty_score = 0
        final_selected_questions = []

        for i in range(len(question_dataset)):
            if question_dataset['diff'][i]==selected_difficulty:
                qp_questions.append(question_dataset['question_id'][i])

        if(has_attempted_questions):
            for i in range(len(user_questions_doc)):
                attempted_questions.append(user_questions_doc[i].questionId)

        tentative_selected_questions = []
        for i in range(len(qp_questions)):
            if(qp_questions[i] not in attempted_questions):
                tentative_selected_questions.append(qp_questions[i])

        number_of_questions = args['marks']/2
        if(len(tentative_selected_questions)==number_of_questions):
            final_selected_questions = tentative_selected_questions
        elif(len(tentative_selected_questions)<number_of_questions):
            #print("length is lesssssssss")
            final_selected_questions = tentative_selected_questions
            for i in range(number_of_questions - len(tentative_selected_questions)):
                final_selected_questions.append(attempted_questions[i])
        else:
            #print("length is moreeeeeeeeeeee SUBTYPE ARGS:", args['subtype'])
            print("No of questions:",number_of_questions,"len:",tentative_selected_questions)
            final_selected_questions = random.sample(tentative_selected_questions, int(number_of_questions))

        question_paper_id = str(uuid.uuid1())
        question_paper_doc = MongoQuestionPaperModel(id=question_paper_id)
        question_paper_doc.exam = 'CET'
        question_paper_doc.marksPerQuestion = 2
        question_paper_doc.date = datetime.datetime.now()
        question_paper_doc.difficulty = selected_difficulty
        question_paper_doc.type = args['subtype']
        question_paper_doc.maxAttempts = -1
        question_paper_doc.totalMarks = args['marks']
        question_paper_doc.duration = args['duration']
        question_paper_doc.questions = str(final_selected_questions)
        question_paper_doc.save()
        return {
            'message': 'Question paper created!',
            'details': {
                'id': question_paper_id,
                'questions': str(final_selected_questions)
            }
        }, 201

    def delete(self):
        return '', 204

class ParticularQuestionPaperServices(Resource):

    def __init__(self) -> None:
        super().__init__()

    #get question paper details
    def get(self, question_paper_id):
        question_paper_doc = MongoQuestionPaperModel.objects(id=question_paper_id)
        if(len(question_paper_doc)==0):
            abort(404, message="This question paper does not exist.")
        return question_paper_doc[0].to_json(), 200

    def post(self, name):
        return name, 202

    def put(self, name):
        return name, 201

    def delete(self, name):
        return '', 204

    def selectQuestions():
        return