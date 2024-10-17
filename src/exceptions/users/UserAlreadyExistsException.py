from src.exceptions.http.ConflictException import ConflictException


class UserAlreadyExistsException(ConflictException):
    pass
