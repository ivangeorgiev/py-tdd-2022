import uuid
from todos.request import AddTodoItemRequest

def test_build_should_return_request_instance():
    params = {
        "todo_list_id": uuid.uuid4(),
        "name": "My Name",
        "correlation_id": uuid.uuid4()
    }

    inst = AddTodoItemRequest.build(**params)

    assert isinstance(inst, AddTodoItemRequest)
    assert inst.todo_list_id == params["todo_list_id"]
    assert inst.name == params["name"]
    assert inst.correlation_id == params["correlation_id"]

