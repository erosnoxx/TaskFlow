from src.domain.entities.users.UserEntity import UserEntity


class CreateUserOutputDto:
    def __init__(self, user_entity: UserEntity) -> None:
        self.user_entity = user_entity
