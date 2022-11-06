from ..request import CreateTodoListRequest
from ..domain.todo_list import TodoList
from ..port.repository import TodoRepository
from ..response import CreateTodoListResponse


def create_todo_list(repo: TodoRepository, request: CreateTodoListRequest):
    todo_list = TodoList(request.name)
    repo.put(todo_list)
    response = CreateTodoListResponse(
        todo_list=todo_list.asdict(),
        request_id=request.id,
        correlation_id=request.correlation_id,
    )
    return response
