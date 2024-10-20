from src.domain.dto.user.input.GetUserInputDto import GetUserInputDto
from src.domain.dto.user.output.GetUserOutputDto import GetUserOutputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.exceptions.users.UserNotExistsException import UserNotExistsException
from src.infra.services.users.UserService import UserService


class GetUserUseCase:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service
    
    def execute(self, input_dto: GetUserInputDto) -> GetUserOutputDto:
        if not isinstance(input_dto.username, str):
            raise InvalidFieldException('O username tem que ser uma string.')
        
        user_entity = self.user_service.find_by_username(username=input_dto.username)
        if user_entity is None:
            raise UserNotExistsException('Usuário não encontrado.')
        return GetUserOutputDto(user_entity=user_entity)
