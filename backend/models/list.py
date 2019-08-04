from db import db

class ListModel(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    tasks = db.relationship('TaskModel', backref='list', lazy='dynamic')

    def __init__(self, title, user_id):
        self.title = title
        self.user_id = user_id

    def json(self):
        return {
            'id':self.id,
            'title':self.title,
            'tasks': [task.json() for task in self.tasks.all()],
            'user_id': self.user_id
    }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()        

    @classmethod
    def find_by_id(cls, list_id):
        return cls.query.get(list_id)

    @classmethod
    def find_all(cls):
        return cls.query.all()    