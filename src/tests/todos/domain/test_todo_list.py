import uuid
from todos.domain.todo_list import TodoList
from todos.domain.todo_item import TodoItem


def test_create_instance_should_set_attributes():
    """
    WHEN todo list instance is created with {"name": "My Todo"}
    THEN new instance shold have `id` attribute with value of UUID type
    And  new instance `name` attribute should equals "My Todo"
    And new instance `items` atttribute is an empty list
    """
    todo = TodoList(name="My Todo")

    assert isinstance(todo.id, uuid.UUID)
    assert todo.name == "My Todo"
    assert todo.items == []


def test_asdict_should_return_dictionary_of_attributes_and_values():
    """
    GIVEN todo list instance with {"name": "My Todo 112"}
    WHEN todo.asdict() method is called
    THEN result should contain {"name": "My Todo 112"}
    """
    todo = TodoList(name="My Todo 112")
    todo.items.append(TodoItem("Drink"))

    assert (
        todo.asdict().items()
        >= {
            "name": "My Todo 112",
        }.items()
    )

    assert todo.asdict()["items"][0].items() >= {"name": "Drink"}.items()


def test_add_item_should_add_todo_item_to_items():
    todo = TodoList(name="My Todo List")
    item = TodoItem(name="Cook")

    todo.add_item(item)
    assert todo.items[0] == item


def test_fromdict_should_return_todolist_instance_with_attributes_set():
    todo_item = TodoItem(name="Just Do It")
    d = {"id": uuid.uuid4(), "name": "My Todo List", "items": [todo_item.asdict()]}
    todo = TodoList.fromdict(d)

    assert todo.id == d["id"]
    assert todo.name == "My Todo List"
    assert todo.items == [todo_item]


def test_fromdict_without_id_should_generate_id():
    d = {"name": "My Todo List"}
    todo = TodoList.fromdict(d)

    assert isinstance(todo.id, uuid.UUID)
