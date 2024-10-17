from datetime import date


class CreatePersonInputDto:
    required_fields = ['first_name', 'last_name', 'birthdate', 'phone_number']
    def __init__(self,
                 first_name: str, 
                 last_name: str, 
                 birthdate: date, 
                 phone_number: str = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.phone_number = phone_number
