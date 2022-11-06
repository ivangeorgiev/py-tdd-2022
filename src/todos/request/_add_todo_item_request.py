import dataclasses
import uuid


@dataclasses.dataclass
class AddTodoItemRequest:
    id: uuid.UUID = dataclasses.field(default_factory=uuid.uuid4, init=False)
    todo_list_id: uuid.UUID
    name: str
    correlation_id: uuid.UUID = dataclasses.field(default=None)

    @classmethod
    def build(
        cls, todo_list_id: uuid.UUID, name: str, correlation_id: uuid.UUID = None
    ) -> "AddTodoItemRequest":
        return cls(todo_list_id=todo_list_id, name=name, correlation_id=correlation_id)
