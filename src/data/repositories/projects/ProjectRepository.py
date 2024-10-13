from requests import Session
from src.application.contracts.data.repositories.projects.IProjectRepository import IProjectRepository
from src.domain.entities.projects.ProjectEntity import ProjectEntity


class ProjectRepository(IProjectRepository):
    def __init__(self, session: Session):
        super().__init__(session, ProjectEntity)
