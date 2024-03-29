from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

classname_post_args = reqparse.RequestParser()
classname_post_args.add_argument("name", type=str, help="Name of the exam is required", required=True)
classname_post_args.add_argument("type", type=str, help="Type of the exam")
classname_post_args.add_argument("year", type=int, help="Year of the exam")

user_services_post_args = reqparse.RequestParser()
user_services_post_args.add_argument("id", type=str, help="User Id is missing")
user_services_post_args.add_argument("name", type=str, help="User name is missing")
user_services_post_args.add_argument("email", type=str, help="Email is missing")
user_services_post_args.add_argument("password", type=str, help="Password is missing")
user_services_post_args.add_argument("phone", type=str, help="Phone is missing")
user_services_post_args.add_argument("user_type", type=str, help="Type is missing")
user_services_post_args.add_argument("attempted_question_papers", type=str, help="Json string for question paper attempts is missing")

particular_user_services_post_args = reqparse.RequestParser()
particular_user_services_post_args.add_argument("id", type=str, help="User Id is missing")
particular_user_services_post_args.add_argument("name", type=str, help="User name is missing", required=True)
particular_user_services_post_args.add_argument("email", type=str, help="Email is missing")
particular_user_services_post_args.add_argument("password", type=str, help="Password is missing")
particular_user_services_post_args.add_argument("type", type=str, help="Type is missing")
particular_user_services_post_args.add_argument("question_paper_attempts", type=str, help="Json string for question paper attempts is missing")

question_paper_services_post_args = reqparse.RequestParser()
question_paper_services_post_args.add_argument("id", type=str, help="Question paper id is required")
question_paper_services_post_args.add_argument("date", type=str, help="Date is missing")
question_paper_services_post_args.add_argument("difficulty", type=int, help="Difficulty is missing")
question_paper_services_post_args.add_argument("duration", type=int, help="Duration is missing")
question_paper_services_post_args.add_argument("type", type=str, help="Type is missing")
question_paper_services_post_args.add_argument("subtype", type=str, help="Subtype is missing")
question_paper_services_post_args.add_argument("marks", type=int, help="Marks is missing")
question_paper_services_post_args.add_argument("questions", type=list, help="Question list is missing")

particular_question_paper_services_post_args = reqparse.RequestParser()
particular_question_paper_services_post_args.add_argument("id", type=str, help="Question paper id is required", required=True)
particular_question_paper_services_post_args.add_argument("date", type=str, help="Date is missing")
particular_question_paper_services_post_args.add_argument("difficulty", type=float, help="Difficulty is missing")
particular_question_paper_services_post_args.add_argument("duration", type=str, help="Duration is missing")
particular_question_paper_services_post_args.add_argument("type", type=str, help="Type is missing")
particular_question_paper_services_post_args.add_argument("subtype", type=type, help="Subtype is missing")
particular_question_paper_services_post_args.add_argument("marks", type=int, help="Marks is missing")
particular_question_paper_services_post_args.add_argument("questions", type=list, help="Question list is missing")

result_services_post_args = reqparse.RequestParser()
result_services_post_args.add_argument("id", type=str, help="ID is missing")
result_services_post_args.add_argument("final_score", type=int, help="Score is required", required=True)
result_services_post_args.add_argument("total_possible_score", type=int, help="Total Score is missing")
result_services_post_args.add_argument("question_wise_results", type=str, help="Questionwise result list is missing")
result_services_post_args.add_argument("time_completed", type=str, help="Time completed is missing")
result_services_post_args.add_argument("total_time_taken", type=int, help="Total time taken is missing") #in minutes

exam_services_post_args = reqparse.RequestParser()
exam_services_post_args.add_argument("user_id", type=str, help="User ID is required", required=True)
exam_services_post_args.add_argument("question_paper_id", type=str, help="Question Paper ID is required", required=True)
exam_services_post_args.add_argument("marks", type=int, help="Total marks for the paper")
exam_services_post_args.add_argument("start_time", type=str, help="Start time is missing")
exam_services_post_args.add_argument("duration", type=str, help="Duration is missing")

particular_question_services_post_args = reqparse.RequestParser()
particular_question_services_post_args.add_argument("user_id", type=str, help="User ID is missing")
particular_question_services_post_args.add_argument("question_id", type=str, help="Question ID is missing")
particular_question_services_post_args.add_argument("question_paper_id_list", type=list, help="Question Paper ID List is missing")
#particular_question_services_post_args.add_argument("attempts", type=int, help="Attempts is missing")
#particular_question_services_post_args.add_argument("max_attempts", type=int, help="Max attempts is missing")
particular_question_services_post_args.add_argument("time_taken", type=int, help="Time taken in seconds is missing")
particular_question_services_post_args.add_argument("correctly_attempted", type=bool, help="Correct attempts is missing")