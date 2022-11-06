
import dataclasses
import uuid

from .todo_item import TodoItem

@dataclasses.dataclass
class TodoList:
    id: uuid.UUID = dataclasses.field(default_factory=uuid.uuid4, init=False)
    name: str
    items: list = dataclasses.field(default_factory=list)

    def asdict(self):
        return dataclasses.asdict(self)

    @classmethod
    def fromdict(cls, dict_attributes: dict):
        kwargs = dict_attributes.copy()
        id = kwargs.pop("id", None)
        items = kwargs.pop("items", [])
        todo = cls(**kwargs)
        if id is not None:
            todo.__dict__["id"] = id
        for item in items:
            todo.items.append(TodoItem.fromdict(item))
        return todo

    def add_item(self, item: TodoItem):
        self.items.append(item)

