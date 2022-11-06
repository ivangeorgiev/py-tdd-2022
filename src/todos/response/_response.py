

import dataclasses
import uuid


@dataclasses.dataclass
class AddTodoItemResponse:
    id: uuid.UUID = dataclasses.field(default_factory=uuid.uuid4, init=False)
    todo_list_id: uuid.UUID
    todo_item: dict
    request_id: uuid.UUID
    correlation_id: uuid.UUID

@dataclasses.dataclass
class CreateTodoListResponse:
    id: uuid.UUID = dataclasses.field(default_factory=uuid.uuid4, init=False)
    todo_list: dict
    request_id: uuid.UUID
    correlation_id: uuid.UUID
