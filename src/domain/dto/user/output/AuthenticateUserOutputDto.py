from src.domain.entities.users.UserEntity import UserEntity


class AuthenticateUserOutputDto:
    def __init__(self, user_entity: UserEntity):
        self.user_entity = user_entity
