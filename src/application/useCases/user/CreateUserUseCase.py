from email_validator import validate_email, EmailNotValidError
from src.domain.dto.user.input.CreateUserInputDto import CreateUserInputDto
from src.domain.dto.user.output.CreateUserOutputDto import CreateUserOutputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.exceptions.users.PersonNotExistsException import PersonNotExistsException
from src.exceptions.users.UserAlreadyExistsException import UserAlreadyExistsException
from src.infra.services.security.HashService import HashService
from src.infra.services.users.PersonService import PersonService
from src.infra.services.users.UserService import UserService
from src.infra.utils.ValidatorsUtil import ValidatorsUtil


class CreateUserUseCase:
    def __init__(self,
                 user_service: UserService,
                 person_service: PersonService,
                 hash_service: HashService) -> None:
        self.user_service = user_service
        self.person_service = person_service
        self.hash_service = hash_service

    def execute(self, person_id: int, input_dto: CreateUserInputDto) -> CreateUserOutputDto:
        try:
            validate_email(input_dto.email)
        except EmailNotValidError as e:
            self.person_service.delete_person_by_id(person_id=person_id)
            raise InvalidFieldException(str(e))
        
        if not ValidatorsUtil.validate_password(password=input_dto.password):
            self.person_service.delete_person_by_id(person_id=person_id)
            raise InvalidFieldException('Senha inválida.')
        
        user_entity = self.user_service.find_email(email=input_dto.email)
        if user_entity is not None:
            self.person_service.delete_person_by_id(person_id=person_id)
            raise UserAlreadyExistsException('Email já registrado.')
        
        user_entity = self.user_service.find_username(username=input_dto.username)
        if user_entity is not None:
            self.person_service.delete_person_by_id(person_id=person_id)
            raise UserAlreadyExistsException('Nome de usuário já registrado.')
        
        person_entity = self.person_service.get_person_by_id(person_id=person_id)
        if person_entity is None:
            raise PersonNotExistsException('person_id não equivale a uma pessoa registrada.')
        
        try:
            hashed_pwd = self.hash_service.hash_password(password=input_dto.password)
            user_entity = self.user_service.create(
                person_id=person_id,
                email=input_dto.email,
                username=input_dto.username,
                password_hash=hashed_pwd)
            
            return CreateUserOutputDto(user_entity=user_entity)
        except ValueError as ve:
            raise InvalidFieldException(str(ve))
        except Exception as e:
            self.person_service.delete_person_by_id(person_id=person_id)
            raise Exception(str(e))
