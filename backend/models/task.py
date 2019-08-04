from db import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    is_finished = db.Column(db.Boolean, default=False)

    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

   

    def __init__(self, body, list_id):
        self.body = body
        self.list_id = list_id

    def json(self):
        return {
            'id':self.id,
            'body':self.body,
            'list_id':self.list_id,
            'is_finished':self.is_finished
    }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()    

    @classmethod
    def find_by_id(cls, task_id):
        return cls.query.get(task_id)    

    @classmethod
    def find_all(cls):
        return cls.query.all()    
    
    @classmethod
    def find_by_list_id(cls, listid):
       return cls.query.filter_by(list_id=listid)  