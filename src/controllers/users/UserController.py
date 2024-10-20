from src.controllers.users import namespace
from src.controllers.users.resources.GetAllUsersResource import GetAllUsersResource
from src.controllers.users.resources.GetUserResource import GetUserResource


class UserController:
    def __init__(self):
        self.namespace = namespace
        self.register_routes()
    
    def register_routes(self) -> None:
        self.namespace.add_resource(GetUserResource, '/<string:username>')
        self.namespace.add_resource(GetAllUsersResource, '/')
