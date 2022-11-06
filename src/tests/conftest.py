from unittest.mock import Mock
import pytest


@pytest.fixture
def mock_todo_repo():
    repo = Mock()
    yield repo
