from src.domain.entities.users.UserEntity import UserEntity


class GetUserOutputDto:
    def __init__(self, user_entity: UserEntity) -> None:
        self.user_entity = user_entity
