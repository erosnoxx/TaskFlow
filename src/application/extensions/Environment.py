import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

class Environment:
    def __init__(self, app: Flask) -> None:
        app.static_folder = os.getenv('STATIC_FOLDER')
        app.template_folder = os.getenv('TEMPLATE_FOLDER')
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
        app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG')
        app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
        app.config['FLASK_APP'] = os.getenv('FLASK_APP')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
