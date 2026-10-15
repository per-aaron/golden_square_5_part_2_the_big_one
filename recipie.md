# Diary/Todo/Directory Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
>As a user
>So that I can record my experiences
>I want to keep a regular diary

>As a user
>So that I can reflect on my experiences
>I want to read my past diary entries

>As a user
>So that I can reflect on my experiences in my busy day
>I want to select diary entries to read based on how much time I have and my reading speed

>As a user
>So that I can keep track of my tasks
>I want to keep a todo list along with my diary

>As a user
>So that I can keep track of my contacts
>I want to see a list of all of the mobile phone numbers in all my diary entries

_How are these numbers attributed to names? Can we assume standardised format in diary entries such as Name: 07xxxxxxxxx . Then store as dictionary object or create a person class?_

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

u"""
┌───────────────────────────────────┐     ┌───────────────────────────────────┐
│ Diary                             │     │ TodoList                          │
│ -entries: [DiaryEntry]            │     │                                   │
│ -todoList: TodoList               │     │                                   │
│ -add(self, entry)                 │     │                                   │
│ -count_words(self)                │has a│                                   │
│ -reading_time(self, wpm)          ├────►│                                   │
│ -find_best_entry(self,wpm,minutes)│     │                                   │
│ -phone_numbers: []                │     │                                   │
│ -list_phone_numbers()             │     │                                   │
│                                   │     │                                   │
└───────────────┬───────────────────┘     └────────────────┬──────────────────┘
                │owns a list of                            │owns a list of     
                │                                          │                   
                ▼                                          ▼                   
┌───────────────────────────────────┐     ┌───────────────────────────────────┐
│ DiaryEntry                        │     │ Todo                              │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
│                                   │     │                                   │
└───────────────────────────────────┘     └───────────────────────────────────┘
"""

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   entries: an array
    #   todoList: TodoList object
    #   

    def __init__(self):
        # Parameters:
        #   None
        # Side-effects:
        #   Initialise entry array and set todoList to None
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def add_todo(self, task):
        # Parameters:
        #   task: string, representing a task
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds a task to the todo list
        pass

    def all(self):
        # Returns:
        #   A list of all entries


    def count_words(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   An integer representing the total number of words in all the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: integer, reading speed of user in words per minute
        # Returns:
        #   Integer representing estimate of reading time for all of the entries using the given wpm
        pass

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
        pass

    def list_phone_numbers(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   A list containing all the phone numbers within diary entries  

class DiaryEntry:
    # User-facing properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents):
        # Parameters:
        #   title: string, title of the entry
        #   contents: string, contents of the entry
        #   progress: integer, reading progress of entry
        # Side-effects:
        #   Sets title and contents properties, init progress to 0
        pass

    def count_words(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: integer, reading speed of user in words per minute
        # Returns:
        #   Integer representing estimate of reading time for the contents using the given wpm
        pass

    def fetch_phone_number(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   A list containing all the phone numbers within this entry
        pass


class TodoList:
    # User-facing properties:
    #   list: an array

    def __init__(self):
        # Parameters:
        #   None
        # Side-effects:
        #   Init list to empty array
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass


    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass


    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
