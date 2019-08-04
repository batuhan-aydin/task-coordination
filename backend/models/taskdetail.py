from db import db

class TaskDetailModel(db.Model):
    __tablename__ = 'taskdetails'

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=False)

    


    def __init__(self, task_id):
        self.task_id = task_id

    def json(self):
        return {
            'is_active':self.is_active,
            'task_id':self.task_id
    }    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  

    @classmethod
    def find_all(cls):
        return cls.query.all()      