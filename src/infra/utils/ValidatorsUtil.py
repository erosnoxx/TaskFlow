import re, os
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()


class ValidatorsUtil:
    @staticmethod
    def phone_number_validator(phone_number: str) -> bool:
        pattern = os.getenv('PHONE_NUMBER_REGEX')
        return re.match(pattern, phone_number) is not None

    @staticmethod
    def validate_password(password: str) -> bool:
        regex = os.getenv('PASSWORD_REGEX')
        if not re.match(regex, password):
            return False
        return True

    @staticmethod
    def validate_input(data: dict, required_fields: List[str]):
        missing_fields = [field for field in required_fields if not data.get(field)]
        return missing_fields
