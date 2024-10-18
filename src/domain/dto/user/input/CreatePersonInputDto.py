from datetime import date
from src.domain.dto.common.BaseInputDto import BaseInputDto


class CreatePersonInputDto(BaseInputDto):
    required_fields = ['first_name', 'last_name', 'birthdate', 'phone_number']
    def __init__(self,
                 first_name: str = None, 
                 last_name: str = None, 
                 birthdate: date = None, 
                 phone_number: str = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.phone_number = phone_number

