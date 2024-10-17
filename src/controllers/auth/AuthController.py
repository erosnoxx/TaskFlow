from src.controllers.auth import namespace
from src.controllers.auth.RegisterResource import RegisterResource


class AuthController:
    def __init__(self):
        self.namespace = namespace
        self.register_routes()
    
    def register_routes(self) -> None:
        self.namespace.add_resource(RegisterResource, '/register_user')
