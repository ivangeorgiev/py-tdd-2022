import uuid
from todos.domain.todo_item import TodoItem


def test_create_should_set_attributes():
    item = TodoItem("Write Blog")

    assert isinstance(item.id, uuid.UUID)
    assert item.name == "Write Blog"


def test_asdict_should_return_dictionary_with_attribute_values():
    todo = TodoItem("Drop Database")

    assert (
        todo.asdict().items()
        >= {
            "name": "Drop Database",
        }.items()
    )


def test_from_dict_should_return_todoitem_with_attributes_set():
    d = {"id": uuid.uuid4(), "name": "Draw It!"}
    todo_item = TodoItem.fromdict(d)

    assert todo_item.id == d["id"]
    assert todo_item.name == d["name"]
