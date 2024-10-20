from typing import List
from src.domain.dto.user.output.GetAllUsersOutputDto import GetAllUsersOutputDto
from src.domain.entities.users.UserEntity import UserEntity
from src.exceptions.users.UserNotExistsException import UserNotExistsException
from src.infra.services.users.UserService import UserService


class GetAllUsersUseCase:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self) -> GetAllUsersOutputDto:
        all_users = self.user_service.find_all_users()
        if not all_users:
            raise UserNotExistsException('Nenhum usuário encontrado.')
        
        return GetAllUsersOutputDto(all_users=all_users)
