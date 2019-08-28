from flask_restful import Resource, reqparse
from models.list import ListModel
from models.user import UserModel
from models.listpermission import ListPermissionModel
from marshmallow import ValidationError
from flask import request
from schemas.list import ListSchema
from schemas.user import UserSchema
from schemas.listpermission import ListPermissionSchema
from db import db
from flask import jsonify

list_schema = ListSchema()
list_schema_many = ListSchema(many=True)
listperm_schema = ListPermissionSchema(many=True)
user_schema = UserSchema()

class List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, help='Cannot be blank!')

    def get(self, list_id):
        ilist = ListModel.find_by_id(list_id)
        if ilist:
            return ilist.json()
        return {"message":"not found"}, 404     

    def put(self, list_id):
        ilist = ListModel.find_by_id(list_id)
        ilist_data = list_schema.load(request.get_json())
        if ilist:
            ilist.title = ilist_data.title
        else:
            ilist_data.save_to_db()
        ilist.save_to_db()
        return list_schema.dump(ilist)

    def delete(self, list_id):
        ilist = ListModel.find_by_id(list_id)
        if ilist:
            ilist.delete_from_db()
            return{"message":"list deleted"}, 200
        return{"message":"list not found"}    



class TodoList(Resource):
               
    def post(self):
        ilist_json = request.get_json()
        user_id = ilist_json["user_id"]
        try:
            ilist = list_schema.load(ilist_json)
        except ValidationError as err:
            return err.messages, 4000 
           
        user = UserModel.find_by_id(user_id)
        ilist.save_to_db()
        perm = ListPermissionModel(user_id=user.id, list_id=ilist.id, role=1)
        perm.save_to_db()
        #ilist.users.append(user)

        return list_schema.dump(ilist), 200

    def get(self):
        items = [item.json() for item in ListModel.find_all()]
        return {"lists":items}
        #return {"lists": [list_schema.dump(ListModel.find_all())]}, 200
    
class UserList(Resource):
    def get(self, user_id):
        #user = UserModel.find_by_id(user_id)
        #result = db.engine.execute("SELECT lists.id, lists.title, listpermissions.user_id FROM lists INNER JOIN listpermissions ON lists.id=listpermissions.list_id")
        result = db.engine.execute("SELECT lists.id, lists.title, listpermissions.user_id FROM lists INNER JOIN listpermissions ON lists.id == listpermissions.list_id WHERE listpermissions.user_id = :val", {'val':user_id})
        #print(lists)
        #print(user)
        #print(user.lists)
        #lists2 = user.lists
        #perms = ListPermissionModel.query.filter_by(user_id=user.id).all()
        #return list_schema.dump(user.lists)
        #items = [item.json() for item in user.list]
        return jsonify({'result': [dict(row) for row in result]})
        #return list_schema_many.dump(lists)