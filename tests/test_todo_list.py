from lib.todo_list import *
import pytest

#On intitialising of todo_list
#We start with empty list
def test_todo_list_init_creates_empty_list():
    my_todo = TodoList()
    assert my_todo.list == []

#Given no incomplete tasks
#Incomplete returns empty list
def test_todo_list_incomplete_returns_empty_list_when_none_incomplete():
    my_todo = TodoList()
    assert my_todo.incomplete() == []

#Given no complete tasks
#Complete returns empty list
def test_todo_list_complete_returns_empty_list_when_none_complete():
    my_todo = TodoList()
    assert my_todo.complete() == []

#Given no tasks
#give_up raises exception
def test_todo_list_give_up_raises_exception_on_empty():
    my_todo = TodoList()
    with pytest.raises(Exception) as e:
        my_todo.give_up()
    assert str(e.value) == "No tasks set!"