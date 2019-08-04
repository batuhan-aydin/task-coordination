from flask_restful import Resource, reqparse
from models.task import TaskModel
from models.taskdetail import TaskDetailModel



class TaskDetailList(Resource):
    def get(self):
        taskdetails = [taskdetail.json() for taskdetail in TaskDetailModel.find_all()]
        return {
            'taskdetails':taskdetails
        }

    def post(self):
        taskdetail = TaskDetailModel(task_id)
        try:
            taskdetail.save_to_db()
        except:
            return {'message':'error during saving'}, 500
        return taskdetail.json(), 200        