from src.controllers.auth import namespace
<<<<<<< HEAD
from src.controllers.auth.resources.RegisterResource import RegisterResource
=======
from src.controllers.auth.RegisterResource import RegisterResource
>>>>>>> main


class AuthController:
    def __init__(self):
        self.namespace = namespace
        self.register_routes()
    
    def register_routes(self) -> None:
        self.namespace.add_resource(RegisterResource, '/register_user')
