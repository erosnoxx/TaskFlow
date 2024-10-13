from requests import Session
from src.application.contracts.data.repositories.users.IUserRepository import IUserRepository
from src.domain.entities.users.UserEntity import UserEntity


class UserRepository(IUserRepository):
    def __init__(self, session: Session):
        super().__init__(session, UserEntity)
