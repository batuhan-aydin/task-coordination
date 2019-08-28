from db import db



class ListPermissionModel(db.Model):
    __tablename__ = 'listpermissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    #user = db.relationship('UserModel', uselist=False)
    #plist = db.relationship('ListModel', uselist=False)
    role = db.Column(db.Integer) # 1 for owner, 2 for shared people
    #user = relationship('UserTable', backref=backref("permissions", cascade="all, delete-orphan"))
    #ilist = relationship('ListTable', backref=backref("permissions", cascade="all, delete-orphan"))


    def __init__(self, user_id: int, list_id: int, role=1):
        self.user_id = user_id
        self.list_id = list_id
        self.role = role

    def json(self):
        return {
            'user_id':self.user_id,
            'list_id':self.list_id,
            'role':self.role
    }


    @classmethod
    def find_by_id(cls, list_id):
        return cls.query.get(list_id)
  

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()    
            
