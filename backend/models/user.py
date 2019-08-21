from db import db
from models.list import ListModel
from models.listpermission import ListPermissionModel
from sqlalchemy.orm import relationship

listperms = db.Table("listperms",
        db.metadata,
        db.Column("id", db.Integer, primary_key = True),
        db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
        db.Column("list_id", db.Integer, db.ForeignKey("lists.id")),
        db.Column("role", db.Integer, default = 1)
        )

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    #lists = db.relationship('ListModel', secondary=listpermissions, lazy='subquery', backref=db.backref('users', lazy=True))
    #lists = db.relationship('ListModel', secondary=listperms, backref=db.backref("users", lazy="dynamic"))
    lists = db.relationship('ListPermissionModel', foreign_keys=[ListPermissionModel.user_id], backref=db.backref('user', lazy='joined'), lazy='dynamic', cascade='all, delete-orphan')
    #perm = relationship('ListPermissionModel', backref=ba'user', primaryjoin=id == ListPermissionModel.user_id)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'id':self.id,
            'username':self.username
        }    


    def save_to_db(self):
        db.session.add(self)
        db.session.commit(),
    
    def delete_from_db(self):    
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_perms_by_user_id(cls, _id):
        #return cls.query.join(listperms).filter_by(role=1).all()
        print(cls.items)
        return cls.lists