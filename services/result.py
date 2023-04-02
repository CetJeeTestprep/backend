import uuid
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import requests
import constants.urls as urls
from schema.mongo_model.mongo_user import MongoUserModel
from schema.mongo_model.mongo_results import MongoResultsModel
from config.parsers import question_paper_services_post_args, particular_question_paper_services_post_args, result_services_post_args

BASE = urls.BASE

def get_qwr_map(qwr_str):
    fields = qwr_str.split(',')
    qwr_map = {}
    for field in fields:
        temp = field.split(':')
        if temp[0] not in ['initial_answer', 'final_answer']:
            qwr_map[temp[0]] = int(temp[1])
        else:
            qwr_map[temp[0]] = temp[1]
    return qwr_map
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

    #add specific question paper results
    def post(self, user_id, question_paper_id):
        return 202

    #add results
    def put(self, user_id):
        return 201

    def delete(self):
        return '', 204
    
class ParticularResultServices(Resource):

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

    #add specific question paper results
    def post(self, user_id, question_paper_id):
        return 202

    #add results
    def put(self, user_id,question_paper_id):
        args = result_services_post_args.parse_args()
        this_user_id = user_id 
        this_question_paper_id = question_paper_id

        confidence_score = 0
        accuracy_score = 0
        attempted_questions = 0
        correctly_attempted_questions = 0

        question_wise_results = args['question_wise_results'].split('##')
        question_wise_results_list = []

        print("--------------------------------------------------")
        print("QWR: ",question_wise_results)
        print("--------------------------------------------------")

        for qwr in question_wise_results:

            qres = get_qwr_map(qwr)

            print("QRES IN RESULTS:",qres)
            question_wise_results_list.append(qres)
            
            if(qres['attempt']!=-1):
                attempted_questions += 1
                if(qres['attempt']==1):
                    correctly_attempted_questions += 1
                    accuracy_score += 1

            if(qres['initial_answer']==qres['final_answer'] and qres['attempt']==1):
                confidence_score += 1

        accuracy_score = (accuracy_score/attempted_questions)*100
        confidence_score = (confidence_score/correctly_attempted_questions)*100

        result_id = str(uuid.uuid1())
        result_doc = MongoResultsModel(id=result_id)
        result_doc.id = result_id
        result_doc.question_paper_id = this_question_paper_id
        result_doc.user_id = this_user_id
        result_doc.final_score  = args['final_score']
        result_doc.total_possible_score = args['total_possible_score']
        result_doc.question_wise_results = question_wise_results_list
        result_doc.time_completed = args['time_completed']
        result_doc.total_time_taken = args['total_time_taken']
        result_doc.confidence_score = confidence_score
        result_doc.accuracy_score = accuracy_score
        result_doc.save()
        return {
            'message': 'Question paper created!',
            'details': {
                'id': result_id,
                'final_score': (args['final_score']/args['total_possible_score'])*100,
                'confidence_score': confidence_score,
                'accuracy_score': accuracy_score
            }
        }, 201

    def delete(self):
        return '', 204
    