from src.controllers.auth.AuthController import AuthController
from src.controllers.users.UserController import UserController


class GlobalControllers:
    def __init__(self):
        self.auth_controller = AuthController()
        self.user_controller = UserController()
