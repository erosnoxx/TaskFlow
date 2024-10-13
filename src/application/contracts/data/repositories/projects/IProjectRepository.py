from abc import ABC
from src.data.repositories.common.BaseRepository import BaseRepository
from src.domain.entities.projects.ProjectEntity import ProjectEntity


class IProjectRepository(ABC, BaseRepository[ProjectEntity]):
    pass
