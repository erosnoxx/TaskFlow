from typing import List
from src.application.contracts.data.repositories.users.IUserRepository import IUserRepository
from src.domain.entities.users.UserEntity import UserEntity


class UserService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository
    
    def create(self,
                 person_id: int,
                 username: str, 
                 email: str, 
                 password_hash: str) -> UserEntity:
        user_entity = UserEntity(
            person_id=person_id,
            username=username,
            email=email,
            password_hash=password_hash)
        return self.user_repository.add(obj=user_entity)

    def find_by_email(self, email: str) -> UserEntity:
        return self.user_repository.get_by_email(email=email)

    def find_by_username(self, username: str) -> UserEntity:
        return self.user_repository.get_by_username(username=username)
    
    def find_by_id(self, user_id: int) -> UserEntity:
        return self.user_repository.get(obj_id=user_id)
    
    def find_all_users(self) -> List[UserEntity]:
        return self.user_repository.get_all()
