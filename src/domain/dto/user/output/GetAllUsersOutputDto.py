from typing import List
from src.domain.entities.users.UserEntity import UserEntity


class GetAllUsersOutputDto:
    def __init__(self, all_users: List[UserEntity]):
        self.all_users = all_users
