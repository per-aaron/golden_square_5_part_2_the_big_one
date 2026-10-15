from lib.todo import *
import pytest

#Given a task
#Initialising todo object stores that task
def test_todo_stores_task():
    task1 = Todo("Walk the dog")
    assert task1.task == "Walk the dog"

#When marking a todo object complete
#Todo object updates completion status to True
def test_todo_can_be_marked_complete():
    task1 = Todo("Walk the dog")
    task1.mark_complete()
    assert task1.complete == True

#Given empty task
#Init raises exception and task is not created
def test_todo_raises_exception_on_empty_task():
    with pytest.raises(Exception) as e:    
        task1 = Todo("")
    assert str(e.value) == "Todo not created, task was empty!"