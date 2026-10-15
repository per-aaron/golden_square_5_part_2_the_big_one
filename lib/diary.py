from lib.todo_list import *

class Diary:
    def __init__(self):
        self.entries = []
        self.todo_list = TodoList()

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def add_todo(self, task):
        # Parameters:
        #   task: string, representing a task
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds a task to the todo list
        self.todo_list.add(task)

    def all(self):
        return self.entries

    def show_todos(self):
        return list(enumerate([todo for todo in self.todo_list.list], start=1))

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_words = 0
        for diary in self.entries:
            total_words += diary.count_words()
        return total_words

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return self.count_words() / wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        closest_time = 0
        best = None
        for diary in self.entries:
            time = diary.reading_time(wpm)
            if time <= minutes and time > closest_time:
                best = diary
                closest_time = time
        return best

    def list_phone_numbers(self):
        return [entry.fetch_phone_number() for entry in self.entries if entry.fetch_phone_number() != None ]

