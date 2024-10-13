from datetime import date
from src.domain.entities.common.BaseEntity import BaseEntity, db


class PersonEntity(BaseEntity):
    __tablename__ = 'persons'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)

    user = db.relationship('UserEntity', uselist=False, back_populates='person')

    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 birthdate: date, 
                 phone_number: str = None) -> None: 
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_birthdate(birthdate)
        self.set_phone_number(phone_number)

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __repr__(self) -> str:
        return '<Person: %r>' % self.full_name

    def set_first_name(self, first_name: str) -> None:
        if not isinstance(first_name, str):
            raise ValueError("O primeiro nome deve ser uma string.")
        if not (1 <= len(first_name) <= 50):
            raise ValueError("O primeiro nome deve ter entre 1 e 50 caracteres.")
        
        self.first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        if not isinstance(last_name, str):
            raise ValueError("O sobrenome deve ser uma string.")
        if not (1 <= len(last_name) <= 50):
            raise ValueError("O sobrenome deve ter entre 1 e 50 caracteres.")
        
        self.last_name = last_name

    def set_birthdate(self, birthdate: date) -> None:
        if not isinstance(birthdate, date):
            raise ValueError("A data de nascimento deve ser um objeto do tipo date.")
        if birthdate >= date.today():
            raise ValueError("A data de nascimento deve ser anterior à data de hoje.")
        
        self.birthdate = birthdate

    def set_phone_number(self, phone_number: str) -> None:
        if phone_number is not None and not isinstance(phone_number, str):
            raise ValueError("O número de telefone deve ser uma string ou None.")
        if phone_number is not None and len(phone_number) > 20:
            raise ValueError("O número de telefone deve ter no máximo 20 caracteres.")
        
        self.phone_number = phone_number
