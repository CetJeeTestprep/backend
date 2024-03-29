import uuid
import pandas as pd
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
        details = ""
        results_for_user_doc = MongoResultsModel.objects(user_id=user_id)
        if(len(results_for_user_doc)==0):
            abort(404, message="No results yet.")
        else:
            message = "Results are as follows!"

            for i in range(len(results_for_user_doc)):
                details = details+"##"+results_for_user_doc[i].id
                # results.append(
                #     {
                #         'id': results_for_user_doc[i].id,
                #         'question_paper_id': results_for_user_doc[i].question_paper_id,
                #         'user_id': results_for_user_doc[i].user_id,
                #         'final_score': results_for_user_doc[i].final_score,
                #         'total_possible_score': results_for_user_doc[i].total_possible_score,
                #         'question_wise_results': results_for_user_doc[i].question_wise_results,
                #         'time_completed': results_for_user_doc[i].time_completed,
                #         'total_time_taken': results_for_user_doc[i].total_time_taken,
                #         'confidence_score': results_for_user_doc[i].confidence_score,
                #         'accuracy_score': results_for_user_doc[i].accuracy_score
                #     }
                # )
            # details = {
            #     'results': results
            # }
                
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
    def get(self, user_id, question_paper_id):
        message = "You have not attempted any tests yet."
        details = "None"
        results = []
        results_for_user_doc = MongoResultsModel.objects(question_paper_id=question_paper_id)
        if(len(results_for_user_doc)==0):
            abort(404, message="No results yet.")
        else:
            message = "Results are as follows!"

            for i in range(len(results_for_user_doc)):
                results.append(
                    {
                        'id': results_for_user_doc[i].id,
                        'question_paper_id': results_for_user_doc[i].question_paper_id,
                        'user_id': results_for_user_doc[i].user_id,
                        'final_score': results_for_user_doc[i].final_score,
                        'total_possible_score': results_for_user_doc[i].total_possible_score,
                        'question_wise_results': results_for_user_doc[i].question_wise_results,
                        'time_completed': str(results_for_user_doc[i].time_completed),
                        'total_time_taken': results_for_user_doc[i].total_time_taken,
                        'confidence_score': results_for_user_doc[i].confidence_score,
                        'accuracy_score': results_for_user_doc[i].accuracy_score
                    }
                )
            details = results
                
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

        user_doc = MongoUserModel.objects.get_or_404(id=user_id)

        past_qp_list = user_doc.attemptedQuestionPapers
        if(past_qp_list!=None):
            past_qp_list.append(result_id)
        else:
            past_qp_list = []
            past_qp_list.append(result_id)

        past_confidence_score = user_doc.confidence_score
        past_accuracy_score = user_doc.accuracy_score
        final_confidence_score = 0
        final_accuracy_score = 0

        if(past_confidence_score!=None):
            final_confidence_score = (confidence_score + past_confidence_score)/2
        else:
            final_confidence_score = confidence_score

        if(past_accuracy_score!=None):
            final_accuracy_score = (accuracy_score + past_accuracy_score)/2
        else:
            final_accuracy_score = accuracy_score

        percent_score = args['final_score']/args['total_possible_score']
        strengths = ""
        weaknesses = ""

        if(percent_score>=0.9 or percent_score<=0.35):
            past_strengths = user_doc.strengths
            past_weaknesses = user_doc.weaknesses

            qid_for_topic = question_wise_results_list[0]['question_id']
            qid_for_topic_str = 'question_id=='+str(qid_for_topic)
            question_dataset = pd.read_csv('https://raw.githubusercontent.com/CetJeeTestprep/backend/main/datasets/matrices_question.csv')
            topic = question_dataset.query(qid_for_topic_str)['topic'][qid_for_topic-1]

            if(percent_score>=0.9):
                if(past_strengths!=None):
                    if topic not in past_strengths:
                        strengths = past_strengths + topic + ', '
                    if past_weaknesses!=None:
                        if topic in past_weaknesses:
                            weaknesses = past_weaknesses.replace(topic+', ','')
                else:
                    strengths = topic + ', '
            
            elif(percent_score<=0.35):
                if(past_weaknesses!=None):
                    if topic not in past_weaknesses:
                        weaknesses = past_weaknesses + topic + ', '
                    if past_strengths!=None:
                        if topic in past_strengths:
                            strengths = past_strengths.replace(topic+', ','')
                else:
                    weaknesses = topic + ', '

            else:
                strengths = past_strengths
                weaknesses = past_weaknesses

        
        user_doc.attemptedQuestionPapers = past_qp_list

        user_doc.update(confidence_score = final_confidence_score)
        user_doc.update(accuracy_score = final_accuracy_score)
        user_doc.update(strengths = strengths)
        user_doc.update(weaknesses = weaknesses)
        #user_doc.update(attempted_question_papers = str(past_qp_list))

        return {
            'message': 'Question paper result stored!',
            'details': {
                'id': result_id,
                'final_score': (args['final_score']/args['total_possible_score'])*100,
                'confidence_score': confidence_score,
                'accuracy_score': accuracy_score,
                'strengths': strengths,
                'weaknesses': weaknesses,
            }
        }, 201

    def delete(self):
        return '', 204
    