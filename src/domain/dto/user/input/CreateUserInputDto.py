class CreateUserInputDto:
    required_fields = ['username', 'email', 'password']
    def __init__(self,
                 username: str,
                 email: str,
                 password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
