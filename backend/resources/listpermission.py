from flask_restful import Resource, reqparse
from models.listpermission import ListPermissionModel
from models.user import UserModel
from db import db
from schemas.listpermission import ListPermissionSchema
from schemas.user import UserSchema
from flask import jsonify, request


perm_schema = ListPermissionSchema(many=True)
user_schema = UserSchema(many=True)


class ListPermission(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=int, required=True, help='Cannot be blank!')
    parser.add_argument('list_id', type=int, required=True, help="Every list needs a list_id." )

    @classmethod
    def get(cls, list_id):
        print(list_id)
        result = db.engine.execute("SELECT users.id, username, role, listpermissions.id, listpermissions.user_id FROM users INNER JOIN listpermissions ON listpermissions.user_id = users.id INNER JOIN lists ON lists.id = listpermissions.list_id WHERE listpermissions.list_id = :val", {'val':list_id})
        return jsonify({'result': [dict(row) for row in result]})
        #permissions = [perm.json() for perm in ListPermissionModel.find_all()]
        #return {'permissions':permissions}

    @classmethod
    def post(cls, list_id):
        data = request.get_json()
        print(data['username'])
        print(list_id)
        user = UserModel.find_by_username(data['username'])
        print(user)
        perm = ListPermissionModel(user.id, list_id, role=2)
        print(perm)
        try:
            perm.save_to_db()
        except:
            return {'message':'error during saving'}, 500 
            
        return perm.json(), 200

    @classmethod
    def delete(cls, list_id):
        # Had to write list_id due to other function
        # But it is actually permission_id
        # It takes the id of pivot, and deletes it
        perm = ListPermissionModel.find_by_id(list_id)
        if perm:
            perm.delete_from_db()
            return {'message':'permission is deleted'}, 200
        return {'message':'permission not found'}, 404    

class Permissions(Resource):
    
    @classmethod
    def get(cls):
        result = ListPermissionModel.query.all()
        return perm_schema.dump(result)