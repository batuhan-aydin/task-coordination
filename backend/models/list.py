from db import db
from typing import List
from models.task import TaskModel
from models.listpermission import ListPermissionModel
from sqlalchemy.orm import relationship

class ListModel(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    tasks = db.relationship("TaskModel", backref="list")
    perm = db.relationship('ListPermissionModel', foreign_keys=[ListPermissionModel.list_id], backref=db.backref('list', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')
    #users = db.relationship('UserModel', secondary='listpermissions')
    #perm = relationship('ListPermissionModel', primaryjoin=id == ListPermissionModel.list_id)

    def __init__(self, title):
        self.title = title

    def json(self):
        return {
            'id':self.id,
            'title':self.title,
            #'tasks': [task.json() for task in self.tasks.all()],
            #'user_id': self.user_id,
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
    def find_all(cls) -> List["ListModel"]:
        return cls.query.all()
