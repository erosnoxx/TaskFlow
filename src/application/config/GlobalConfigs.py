from flask import Flask
from src.application.extensions.Environment import Environment
from src.application.extensions.Management import Management


class GlobalConfigs:
    def __init__(self, app: Flask) -> None:
        environment = Environment(app=app)
        management = Management(app=app)
