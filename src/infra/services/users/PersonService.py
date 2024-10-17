from datetime import date
from src.application.contracts.data.repositories.users.IPersonRepository import IPersonRepository
from src.domain.entities.users.PersonEntity import PersonEntity


class PersonService:
    def __init__(self, 
                 person_repository: IPersonRepository) -> None:
        self.person_repository = person_repository

    def create(self,
                 first_name: str, 
                 last_name: str, 
                 birthdate: date, 
                 phone_number: str = None) -> PersonEntity:
        person_entity = PersonEntity(
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            phone_number=phone_number)
        return self.person_repository.add(obj=person_entity)
    
    def get_person_by_id(self, person_id: int) -> PersonEntity:
        return self.person_repository.get(obj_id=person_id)

    def delete_person_by_id(self, person_id: int) -> bool:
        try:
            self.person_repository.delete(obj_id=person_id)
            return True
        except Exception:
            return False
