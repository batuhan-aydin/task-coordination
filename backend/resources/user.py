from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
from blacklist import BLACKLIST
from marshmallow import ValidationError
from schemas.user import UserSchema
from schemas.list import ListSchema
from flask import request, session
from models.list import ListModel
from models.listpermission import ListPermissionModel
from schemas.listpermission import ListPermissionSchema


user_schema = UserSchema()
user_schema_many = UserSchema(many=True)
list_schema = ListSchema(many=True)
perm_schema = ListPermissionSchema()

class UserRegister(Resource):

    def post(self):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_username(user.username):
            return {"message": "A user with that username already exists"}, 400
   
        user.save_to_db()
        
        thelist = ListModel("Gelen Kutusu")
        thelist.save_to_db()
        permission = ListPermissionModel(user.id, thelist.id)
        
        permission.save_to_db()
        #return {"message": "User created successfully."}, 201
        return perm_schema.dump(permission)

class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'user not found'}, 404
        return user_schema.dump(user)

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return{'message':'user not found'}, 404
        user.delete_from_db()  
        return {'message':'user deleted'}  

class UserLogin(Resource):

    @classmethod                    
    def post(cls):
        try:
            user_data = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user.password, user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True) 
            refresh_token = create_refresh_token(user.id) 
            return {
                'access_token':access_token,
                'refresh_token':refresh_token,
                'user':user_schema.dump(user)
            }, 200
        return {'message':'invalid credentials'}, 401       


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200           
