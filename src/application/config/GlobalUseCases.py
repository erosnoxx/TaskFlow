from src.application.config.GlobalServices import GlobalServices
from src.application.useCases.user.AuthenticateUserUseCase import AuthenticateUserUseCase
from src.application.useCases.user.CreatePersonUseCase import CreatePersonUseCase
from src.application.useCases.user.CreateUserUseCase import CreateUserUseCase
from src.application.useCases.user.GetAllUsersUseCase import GetAllUsersUseCase
from src.application.useCases.user.GetUserUseCase import GetUserUseCase


class GlobalUseCases:
    def __init__(self, services: GlobalServices):
        self.create_person_usecase = CreatePersonUseCase(person_service=services.person_service)
        self.create_user_usecase = CreateUserUseCase(
            user_service=services.user_service,
            person_service=services.person_service,
            hash_service=services.hash_service)
        self.authenticate_user_usecase = AuthenticateUserUseCase(
            user_service=services.user_service,
            hash_service=services.hash_service)
        self.get_user_usecase = GetUserUseCase(user_service=services.user_service)
        self.get_all_users_usecase = GetAllUsersUseCase(user_service=services.user_service)
