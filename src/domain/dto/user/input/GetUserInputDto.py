from src.domain.dto.common.BaseInputDto import BaseInputDto


class GetUserInputDto(BaseInputDto):
    required_fields = ['username']
    def __init__(self, username: str):
        self.username = username
