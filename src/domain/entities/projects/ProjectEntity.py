from datetime import date
from src.domain.entities.common.BaseEntity import BaseEntity, db, schema


class ProjectEntity(BaseEntity):
    __tablename__ = 'projects'

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.ForeignKey(f'{schema}.users.id'), nullable=False)

    owner = db.relationship('UserEntity', back_populates='projects')

    def __init__(self, 
                 name: str, 
                 start_date: date, 
                 status: str, 
                 description: str = None, 
                 end_date: date = None) -> None:
        self.set_name(name)
        self.set_start_date(start_date)
        self.set_status(status)
        self.set_description(description)
        self.set_end_date(end_date)

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("O nome do projeto deve ser uma string.")
        if not (1 <= len(name) <= 100):
            raise ValueError("O nome do projeto deve ter entre 1 e 100 caracteres.")
        
        self.name = name

    def set_description(self, description: str) -> None:
        if description is not None and not isinstance(description, str):
            raise ValueError("A descrição do projeto deve ser uma string ou None.")
        self.description = description

    def set_start_date(self, start_date: date) -> None:
        if not isinstance(start_date, date):
            raise ValueError("A data de início deve ser um objeto do tipo date.")
        if start_date > date.today():
            raise ValueError("A data de início não pode ser no futuro.")
        
        self.start_date = start_date

    def set_end_date(self, end_date: date) -> None:
        if end_date is not None and not isinstance(end_date, date):
            raise ValueError("A data de término deve ser um objeto do tipo date ou None.")
        if end_date is not None and end_date < self.start_date:
            raise ValueError("A data de término deve ser posterior à data de início.")
        
        self.end_date = end_date

    def set_status(self, status: str) -> None:
        if not isinstance(status, str):
            raise ValueError("O status deve ser uma string.")
        if status not in ['active', 'paused', 'completed', 'cancelled']:
            raise ValueError("O status deve ser 'active', 'paused', 'completed' ou 'cancelled'.")
        
        self.status = status

    def __repr__(self) -> str:
        return f'<Project: {self.name}>'
