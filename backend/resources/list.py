from flask_restful import Resource, reqparse
from models.list import ListModel
from models.user import UserModel


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
        data = List.parser.parse_args()
        if ilist:
            ilist.title = data['title']
        else:
            ilist = ListModel(data['title'])
        ilist.save_to_db()
        return ilist.json()

    def delete(self, list_id):
        ilist = ListModel.find_by_id(list_id)
        if ilist:
            ilist.delete_from_db()
            return{"message":"list deleted"}, 200
        return{"message":"list not found"}    



class TodoList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, help='Cannot be blank!')
    parser.add_argument('user_id', type=int, required=True, help="Every list needs a user_id." )
                    
    def post(self):
        data = TodoList.parser.parse_args()
        ilist = ListModel(data['title'], data['user_id'])
        try:
            ilist.save_to_db()
        except:
            return {'message':'error during saving'}, 500
        return ilist.json(), 200

    def get(self):
        items = [item.json() for item in ListModel.find_all()]
        return {"lists":items}
    
class UserList(Resource):
    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        items = [item.json() for item in user.lists]
        return {"lists":items}