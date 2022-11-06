import abc
from typing import List
import uuid

from ...domain import TodoList

class TodoRepository(abc.ABC):

    @abc.abstractmethod
    def get(self, id: uuid.UUID) -> TodoList:
        """Get TodoList instance from repository"""

    @abc.abstractmethod
    def put(self, todo: TodoList):
        """Put TodoList instance into repository"""

    @abc.abstractmethod
    def list(self) -> List[TodoList]:
        """Get list of all TodoList-s stored in the repository"""
