from src.application.config.GlobalRepositories import GlobalRepositories
from src.infra.services.security.CryptService import CryptService
from src.infra.services.security.HashService import HashService
from src.infra.services.users.PersonService import PersonService
from src.infra.services.users.UserService import UserService


class GlobalServices:
    def __init__(self,
                 repositories: GlobalRepositories) -> None:
        self.hash_service = HashService()
        self.crypt_service = CryptService()
        self.person_service = PersonService(person_repository=repositories.person_repository)
        self.user_service = UserService(user_repository=repositories.user_repository)
    