from lib.todo import *
from lib.todo_list import *

#Given a todo object
#Todo_list add can add the todo to a list of tasks
def test_todo_list_add_adds_task_to_list():
    task1 = Todo("Walk the dog")
    my_todo = TodoList()
    my_todo.add(task1)
    assert my_todo.list == [task1]

#Given a mix of complete and incomplete tasks
#Todo_list incomplete returns a list of only the incomplete tasks
def test_todo_list_incomplete_returns_all_incomplete_tasks():
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the frog")
    task3 = Todo("Walk the zard")
    task4 = Todo("Walk the bard")
    my_todo = TodoList()
    my_todo.add(task1)
    my_todo.add(task2)
    my_todo.add(task3)
    my_todo.add(task4)
    task1.mark_complete()
    task4.mark_complete()
    assert my_todo.incomplete() == [task2, task3]

#Given a mix of complete and incomplete tasks
#Todo_list complete returns a list of only the complete tasks
def test_todo_list_complete_returns_all_complete_tasks():
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the frog")
    task3 = Todo("Walk the zard")
    task4 = Todo("Walk the bard")
    my_todo = TodoList()
    my_todo.add(task1)
    my_todo.add(task2)
    my_todo.add(task3)
    my_todo.add(task4)
    task1.mark_complete()
    task4.mark_complete()
    assert my_todo.complete() == [task1, task4]

#Given a list of task within todo_list
#Todo_list give_up marks all tasks as complete
#And all tasks are returned by complete()
    task1 = Todo("Walk the dog")
    task2 = Todo("Walk the frog")
    task3 = Todo("Walk the zard")
    task4 = Todo("Walk the bard")
    my_todo = TodoList()
    my_todo.add(task1)
    my_todo.add(task2)
    my_todo.add(task3)
    my_todo.add(task4)
    my_todo.give_up()
    assert my_todo.complete() == [task1, task2, task3, task4]
