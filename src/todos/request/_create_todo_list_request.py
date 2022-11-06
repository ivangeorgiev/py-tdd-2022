import dataclasses
import uuid


@dataclasses.dataclass(frozen=True)
class CreateTodoListRequest:
    id: uuid.UUID = dataclasses.field(default_factory=uuid.uuid4, init=False)
    name: str
    correlation_id: uuid.UUID = dataclasses.field(default=None)

    @classmethod
    def build(cls, name: str, correlation_id: uuid.UUID = None) -> "CreateTodoListRequest":
        return CreateTodoListRequest(name=name, correlation_id=correlation_id)
