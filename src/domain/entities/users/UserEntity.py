from flask_login import UserMixin
from src.domain.entities.common.BaseEntity import (
    BaseEntity, db, schema)


class UserEntity(BaseEntity, UserMixin):
    __tablename__ = 'users'

    person_id = db.Column(db.ForeignKey(f'{schema}.persons.id'))
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    person = db.relationship('PersonEntity', uselist=False, back_populates='user')
    projects = db.relationship('ProjectEntity', uselist=False, back_populates='owner')

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    def __init__(self,
                 person_id: int,
                 username: str, 
                 email: str, 
                 password_hash: str) -> None:
        self.set_person_id(person_id=person_id)
        self.set_username(username=username)
        self.set_email(email=email)
        self.set_password(password_hash=password_hash)

    def __repr__(self) -> str:
        return '<User: %r>' % self.username

    def set_person_id(self, person_id: int) -> None:
        if not isinstance(person_id, int):
            raise ValueError('O person id deve ser um inteiro.')

        self.person_id = person_id

    def set_username(self, username: str) -> None:
        if not isinstance(username, str):
            raise ValueError("O nome de usuário deve ser uma string.")
        if not (3 <= len(username) <= 15):
            raise ValueError("O nome de usuário deve ter entre 3 e 15 caracteres.")

        self.username = username
    
    def set_email(self, email: str) -> None:
        if not isinstance(email, str):
            raise ValueError("O email deve ser uma string.")
        
        if not (4 <= len(email) < 255):
            raise ValueError("O email deve ter no entre 4 e 255 caracteres.")

        self.email = email

    def set_password(self, password_hash: str) -> None:
        if not isinstance(password_hash, str):
            raise ValueError("A senha deve ser uma string.")
        if len(password_hash) > 255:
            raise ValueError("A senha deve ter no máximo 255 caracteres.")

        self.password_hash = password_hash
