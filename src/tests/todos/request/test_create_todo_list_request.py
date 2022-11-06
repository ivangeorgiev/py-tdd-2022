import uuid
from todos.request import CreateTodoListRequest

def test_build_should_return_request_instance():
    params = {
        "name": "My Name",
        "correlation_id": uuid.uuid4()
    }

    inst = CreateTodoListRequest.build(**params)

    assert inst.name == params["name"]
    assert inst.correlation_id == params["correlation_id"]

