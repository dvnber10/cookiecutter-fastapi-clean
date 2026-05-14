from ...application.interfaces.i_repositories.base_repo_interface import IRepository
from sqlalchemy.orm import Session
from typing import Type, TypeVar, Optional, List

T = TypeVar('T')

class BaseRepository(IRepository[T]):
    def __init__(self, db: Session, model_class: Type):
        self.db = db
        self.model = model_class

    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def list_all(self) -> List[T]:
        return self.db.query(self.model).all()