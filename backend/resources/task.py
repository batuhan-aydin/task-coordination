from flask_restful import Resource, reqparse
from models.task import TaskModel
from marshmallow import ValidationError
from schemas.task import TaskSchema
from flask import request


task_schema = TaskSchema()

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('body', type=str, help='Cannot be blank!')
    parser.add_argument('is_finished', type=bool, help="is_finished")

    def get(self, task_id):
        task = TaskModel.find_by_id(task_id)
        if task:
            return task.json()
        return{'message':'not found'}, 404

    def put(self, task_id):
        task = TaskModel.find_by_id(task_id)
        data = Task.parser.parse_args()
        if task:
            task.is_finished = data['is_finished']
        else:
            task = TaskModel(data['body'], data['list_id'])
        task.save_to_db()
        return task.json()

    def delete(self, task_id):
        task = TaskModel.find_by_id(task_id)
        if task:
            task.delete_from_db()
            return{"message":"list deleted"}, 200
        return{"message":"list not found"}   

class TaskList(Resource):
  
    def post(self):
        try:
            task = task_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400    

        try:
            task.save_to_db()
        except:
            return {'message':'error during saving'}, 500
        return task_schema.dump(task), 200

    def get(self):
        tasks = [task.json() for task in TaskModel.find_all()]
        return {'tasks':tasks}

class TaskByList(Resource):
    def get(self, list_id):
        tasks = [task.json() for task in TaskModel.find_by_list_id(list_id)]
        return {'tasks':tasks}