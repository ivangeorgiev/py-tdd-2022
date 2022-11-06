from .. import domain
from ..port.repository import TodoRepository
from ..request import AddTodoItemRequest
from ..response import AddTodoItemResponse


def add_todo_item(
    repo: TodoRepository, request: AddTodoItemRequest
) -> AddTodoItemResponse:
    todo_list = repo.get(id=request.todo_list_id)
    todo_item = domain.TodoItem(name=request.name)
    todo_list.add_item(todo_item)
    repo.put(todo=todo_list)
    response = AddTodoItemResponse(
        todo_list_id=request.todo_list_id,
        todo_item=todo_item.asdict(),
        request_id=request.id,
        correlation_id=request.correlation_id,
    )
    return response
