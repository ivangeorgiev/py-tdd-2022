
from unittest.mock import Mock
import uuid
from todos.request import CreateTodoListRequest
from todos.response import CreateTodoListResponse
from todos.usecase import create_todo_list

def test_create_todo_list_usecase_creates_todo_list(mock_todo_repo:Mock):
    request = CreateTodoListRequest("My Todo", correlation_id=uuid.uuid4())
    response = create_todo_list(mock_todo_repo, request)

    mock_todo_repo.put.assert_called()
    assert isinstance(response, CreateTodoListResponse)
    assert response.todo_list["name"] == "My Todo"
    assert response.correlation_id == request.correlation_id
    assert response.request_id == request.id
