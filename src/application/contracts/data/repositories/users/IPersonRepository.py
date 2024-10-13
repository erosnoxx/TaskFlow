from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.users.PersonEntity import PersonEntity


class IPersonRepository(ABC, BaseRepository[PersonEntity]):
    pass
