from unittest.mock import Mock, patch
import uuid
from todos.response import AddTodoItemResponse
from todos.usecase import add_todo_item


@patch("todos.domain.TodoItem")
def test_add_todo_item_usecase_creates_todo_list(todoitem_mock, mock_todo_repo: Mock):
    # Given existing TodoList
    todo_list = Mock()
    todo_list.id = uuid.uuid4()

    mock_todo_repo.get.return_value = todo_list

    # This will be returned as TodoItem instance
    todo_item = Mock()
    todoitem_mock.return_value = todo_item

    # Given request
    request = Mock()

    response = add_todo_item(mock_todo_repo, request)

    mock_todo_repo.get.assert_called_with(id=request.todo_list_id)
    todo_list.add_item.assert_called_with(todo_item)
    mock_todo_repo.put.assert_called_with(todo=todo_list)
    assert isinstance(response, AddTodoItemResponse)
    assert response.todo_list_id == request.todo_list_id
    assert response.todo_item is todo_item.asdict.return_value
    assert response.request_id == request.id
    assert response.correlation_id == request.correlation_id
