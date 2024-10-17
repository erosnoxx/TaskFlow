from datetime import datetime
from src.domain.dto.user.input.CreatePersonInputDto import CreatePersonInputDto
from src.domain.dto.user.output.CreatePersonOutputDto import CreatePersonOutputDto
from src.exceptions.users.InvalidFieldException import InvalidFieldException
from src.infra.services.users.PersonService import PersonService
from src.infra.utils.ValidatorsUtil import ValidatorsUtil


class CreatePersonUseCase:
    def __init__(self,
                 person_service: PersonService) -> None:
        self.person_service = person_service
    
    def execute(self, input_dto: CreatePersonInputDto) -> CreatePersonOutputDto:
        if (input_dto.phone_number and
                not ValidatorsUtil.phone_number_validator(
                    phone_number=input_dto.phone_number)):
            raise InvalidFieldException('Número de telefone inválido.')

        try:
            person_entity = self.person_service.create(
                first_name=input_dto.first_name,
                last_name=input_dto.last_name,
                birthdate=datetime.strptime(input_dto.birthdate, '%Y-%m-%d').date(),
                phone_number=input_dto.phone_number)

            return CreatePersonOutputDto(person_entity=person_entity)
        except ValueError as ve:
            raise InvalidFieldException(str(ve))
        except Exception as e:
            raise Exception(str(e))
