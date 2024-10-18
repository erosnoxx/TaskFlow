from src.domain.dto.common.BaseInputDto import BaseInputDto


class CreateUserInputDto(BaseInputDto):
    required_fields = ['username', 'email', 'password']
    def __init__(self,
                 username: str=None,
                 email: str=None,
                 password: str=None) -> None:
        self.username = username
        self.email = email
        self.password = password
