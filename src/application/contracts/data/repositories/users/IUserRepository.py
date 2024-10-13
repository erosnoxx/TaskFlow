from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.users.UserEntity import UserEntity


class IUserRepository(ABC, BaseRepository[UserEntity]):
    pass
