class TodoList:
    def __init__(self):
        self.list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_tasks = [todo for todo in self.list if todo.complete == False]
        return incomplete_tasks


    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_tasks = [todo for todo in self.list if todo.complete == True]
        return complete_tasks


    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        if self.list == []:
            raise Exception("No tasks set!")
        for todo in self.list:
            todo.mark_complete()
