import uuid
from todos.response import CreateTodoListResponse

def test_me():
    args = {
        "todo_list": {},
        "request_id": uuid.uuid4(),
        "correlation_id": uuid.uuid4()
    }

    response = CreateTodoListResponse(**args)

    assert isinstance(response.id, uuid.UUID)
    assert response.todo_list is args["todo_list"]
    assert response.request_id == args["request_id"]
    assert response.correlation_id == args["correlation_id"]
