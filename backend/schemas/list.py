from ma import ma
from models.list import ListModel
from schemas.user import UserSchema
from marshmallow import INCLUDE


class ListSchema(ma.ModelSchema):
    users = ma.Nested(UserSchema, many=True)

    class Meta:
        model = ListModel
        dump_only=("id",)
        unknown = INCLUDE


