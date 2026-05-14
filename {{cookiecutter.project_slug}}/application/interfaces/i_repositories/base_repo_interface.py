from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class IRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]: ...
    @abstractmethod
    def list_all(self) -> List[T]: ...