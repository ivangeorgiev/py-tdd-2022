
import dataclasses
import uuid


@dataclasses.dataclass(frozen=True)
class TodoItem:
    id: uuid.UUID = dataclasses.field(default_factory=uuid.uuid4, init=False)
    name: str

    def asdict(self):
        return dataclasses.asdict(self)

    @classmethod
    def fromdict(cls, atributes: dict):
        kwargs = atributes.copy()
        id = kwargs.pop("id", None)
        item = TodoItem(**kwargs)
        if id is not None:
            item.__dict__["id"] = id
        return item
