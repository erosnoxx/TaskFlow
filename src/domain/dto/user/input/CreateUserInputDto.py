class CreateUserInputDto:
    required_fields = ['username', 'email', 'password']
    def __init__(self,
                 username: str=None,
                 email: str=None,
                 password: str=None) -> None:
        self.username = username
        self.email = email
        self.password = password

    def set_attributes(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
