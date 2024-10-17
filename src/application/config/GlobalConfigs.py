from flask import Flask
from src.application.extensions.Api import Api
from src.application.extensions.Environment import Environment
from src.application.extensions.Management import Management
from src.application.extensions.Settings import Settings


class GlobalConfigs:
    def __init__(self, app: Flask) -> None:
        Environment(app=app)
        Management(app=app)
        Settings(app=app)
        Api(app=app)
