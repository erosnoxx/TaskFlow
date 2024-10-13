from requests import Session
from src.application.contracts.data.repositories.users.IPersonRepository import IPersonRepository
from src.domain.entities.users.PersonEntity import PersonEntity


class PersonRepository(IPersonRepository):
    def __init__(self, session: Session):
        super().__init__(session, PersonEntity)
