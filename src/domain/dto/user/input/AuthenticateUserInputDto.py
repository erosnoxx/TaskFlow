from src.domain.dto.common.BaseInputDto import BaseInputDto


class AuthenticateUserInputDto(BaseInputDto):
    required_fields = ['password']
    def __init__(self,
                username: str=None,
                email: str=None,
                password: str=None):
        self.username = username
        self.email = email
        self.password = password

    def validate(self):
        if not self.username and not self.email:
            raise ValueError('É necessário fornecer o username ou o email para login.')
