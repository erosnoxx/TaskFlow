from email_validator import validate_email, EmailNotValidError
from src.domain.dto.user.input.AuthenticateUserInputDto import AuthenticateUserInputDto
from src.domain.dto.user.output.AuthenticateUserOutputDto import AuthenticateUserOutputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.exceptions.users.InvalidPasswordException import InvalidPasswordException
from src.exceptions.users.UserNotExistsException import UserNotExistsException
from src.infra.services.security.HashService import HashService
from src.infra.services.users.UserService import UserService
from src.infra.utils.ValidatorsUtil import ValidatorsUtil


class AuthenticateUserUseCase:
    def __init__(self,
                user_service: UserService,
                hash_service: HashService):
        self.user_service = user_service
        self.hash_service = hash_service
    
    def execute(self,
                input_dto: AuthenticateUserInputDto) -> AuthenticateUserOutputDto:
        try:
            input_dto.validate()
            user_entity = None

            if not ValidatorsUtil.validate_password(password=input_dto.password):
                raise InvalidFieldException('Senha inválida.')

            if input_dto.email:
                validate_email(input_dto.email)
                user_entity = self.user_service.find_by_email(email=input_dto.email)
                if user_entity is None:
                    raise UserNotExistsException('Email não registrado.')
            elif input_dto.username:
                user_entity = self.user_service.find_by_username(username=input_dto.username)
                if user_entity is None:
                    raise UserNotExistsException('Username não registrado.')

            if user_entity is not None and not self.hash_service.verify_password(
                hashed_password=user_entity.password_hash,
                provided_password=input_dto.password):
                raise InvalidPasswordException('Senha incorreta.')

            return AuthenticateUserOutputDto(user_entity=user_entity)
        except (ValueError, EmailNotValidError) as e:
                raise InvalidFieldException(str(e))
