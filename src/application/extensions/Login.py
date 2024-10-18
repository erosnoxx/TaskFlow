from flask import Flask
from src.application.extensions.Management import lm
from src.domain.entities.users.UserEntity import UserEntity


class Login:
    def __init__(self, app: Flask):
        lm.init_app(app=app)

        @lm.user_loader
        def load_user(user_id):
            return UserEntity.query.get(user_id)
