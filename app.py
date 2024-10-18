from flask import Flask
from dynaconf import FlaskDynaconf


class App:
    def create_app(self) -> Flask:
        app = Flask(__name__)
        FlaskDynaconf(app=app, extensions_list=True)
        return app

app = App().create_app()

if __name__ == '__main__':
    app.run(debug=True)
