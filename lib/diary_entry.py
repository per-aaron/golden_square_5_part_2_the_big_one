# File: lib/diary_entry.py
import re

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.progress = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        if len(self.contents) > 0:
            return len(self.contents.split())
        else:
            return 0

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        if self.progress >= self.count_words(): #check if we have previouslt already reached end of text
            self.progress = 0 #if not set progress to start of text
        last_word = wpm * minutes + self.progress #calculates position of final word by adding number of words readable to current progress
        chunk = self.contents.split()[self.progress:last_word] #previously for looped this and added to string, but this is simpler
        self.progress += last_word - self.progress #Calculate change in progress by the difference between last word and previous progress. Note can result over length of text, but covered by line 46
        return " ".join(chunk)

    def fetch_phone_number(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   A list containing all the phone numbers within this entry
        numbers = re.search(r"[^ ]+:\s?[0-9]{1,4}[-\s\./0-9]{6,11}$",self.contents)
        if numbers is None:
            return None
        return numbers.group()