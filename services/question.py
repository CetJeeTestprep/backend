from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from schema.mongo_model.mongo_users_questions import MongoUserQuestionsModel
from config.parsers import particular_question_services_post_args

def convertStringToList(s):
    length = len(s)
    s_stripped = s[1:length-1]
    l = s_stripped.split(', ')
    cleanL = []

    for li in l:
        liLength = len(li)
        cleanLi = li[1:liLength-1]
        cleanL.append(cleanLi)

    return cleanL
class ParticularQuestionServices(Resource):

    def __init__(self) -> None:
        super().__init__()

    def get(self, name):
        return name, 200

    def post(self, name):
        return name, 202

    #add user-question association
    def put(self, user_id, question_paper_id, question_id):
        args = particular_question_services_post_args.parse_args()
        this_user_id = user_id
        this_question_paper_id = question_paper_id
        this_question_id = question_id

        user_questions_preexisting_doc = MongoUserQuestionsModel.objects(id=this_user_id+"##"+this_question_id)
        user_questions_doc = MongoUserQuestionsModel(id=this_user_id+"##"+this_question_id)
        user_questions_doc.userId = this_user_id
        user_questions_doc.questionId = this_question_id

        if(len(user_questions_preexisting_doc)==0):
            user_questions_doc.questionPaperIds = str([this_question_paper_id])
            user_questions_doc.attempts = 1
            user_questions_doc.leastTimeTaken = args['time_taken']
            user_questions_doc.mostTimeTaken = args['time_taken']
            if(args['correctly_attempted']):
                user_questions_doc.correctAttempts = 1
                user_questions_doc.incorrectAttempts = 0
            else:
                user_questions_doc.correctAttempts = 0
                user_questions_doc.incorrectAttempts = 1
        else:
            attempts = user_questions_preexisting_doc[0].attempts + 1

            question_paper_ids_list = convertStringToList(user_questions_preexisting_doc[0].questionPaperIds)
            if(this_question_paper_id not in question_paper_ids_list):
                question_paper_ids_list.append(this_question_paper_id)

            correctAttempts = user_questions_preexisting_doc[0].correctAttempts
            incorrectAttempts = user_questions_preexisting_doc[0].incorrectAttempts

            if(int(user_questions_preexisting_doc[0].leastTimeTaken)>int(args['time_taken'])):
                user_questions_doc.leastTimeTaken = args['time_taken']
                user_questions_doc.mostTimeTaken = user_questions_preexisting_doc[0].mostTimeTaken
            elif(int(user_questions_preexisting_doc[0].mostTimeTaken)<int(args['time_taken'])):
                user_questions_doc.mostTimeTaken = args['time_taken']
                user_questions_doc.leastTimeTaken = user_questions_preexisting_doc[0].leastTimeTaken
            
            if(args['correctly_attempted']):
                correctAttempts += 1
            else:
                incorrectAttempts +=1

            user_questions_doc.attempts = attempts
            user_questions_doc.correctAttempts = correctAttempts
            user_questions_doc.incorrectAttempts = incorrectAttempts
            user_questions_doc.questionPaperIds = str(question_paper_ids_list)

        user_questions_doc.save()
            
        return {
            'message': 'User Question association saved.',
            'details': {
                'id': this_user_id+"##"+this_question_id,
            }
        }, 201

    def delete(self, name):
        return '', 204