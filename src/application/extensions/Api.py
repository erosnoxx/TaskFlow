from flask import Flask
from flask_restx import Api

api = Api(prefix='/developers/api/v1/', doc='/developers/api/v1/docs/')

class Api:
    def __init__(self, app: Flask):
        api.init_app(app=app)
        api.add_namespace(app.controllers.auth_controller.namespace)
