from sqlalchemy.orm import Session
from src.application.extensions.Management import db
from src.data.repositories.users.PersonRepository import PersonRepository
from src.data.repositories.users.UserRepository import UserRepository


class GlobalRepositories:
    def __init__(self):
        _session: Session = db.session
        self.person_repository = PersonRepository(session=_session)
        self.user_repository = UserRepository(session=_session)
