from ma import ma
from models.listpermission import ListPermissionModel


class ListPermissionSchema(ma.ModelSchema):
    class Meta:
        model = ListPermissionModel

