from typing import Generic, TypeVar, List, Optional
from repositories.base_repository import BaseRepository

T = TypeVar('T')

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def get_all(self) -> List[T]:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> Optional[T]:
        return self.repository.get_by_id(id)

    def create(self, entity: T) -> T:
        return self.repository.create(entity)

    def update(self, entity: T) -> T:
        return self.repository.update(entity)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)
