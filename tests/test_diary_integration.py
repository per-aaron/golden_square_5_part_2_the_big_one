from lib.diary import *
from lib.diary_entry import *
from lib.todo_list import *
from lib.todo import *



#Given two diary entries
#All returns a list with both instances/titles
def test_diary_returns_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry("Chapter 1", "This is text")
    entry2 = DiaryEntry("Chapter 2", "This is also text")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

#Given three diary entries
#count_words returns the total number of words across all 3 entries
def test_diary_count_returns_number_of_words_including_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("Awakening 1", "Oh... It's you. It's been a long time. How have you been?")
    entry2 = DiaryEntry("Awakening 2", "I've been really busy being dead. You know, after you MURDERED ME.")
    entry3 = DiaryEntry("Awakening 3", "Okay. Look. We both said a lot of things that you're going to regret. But I think we can put our differences behind us. For science. You monster.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.count_words() == 52

#Given three diary entries
#reading_time returns the total minutes required to read all 3 entries
def test_diary_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("Incinerator 1", "Here we are. The Incinerator Room. Be careful not to trip over any parts of me that didn't get completely burned when you threw them down here.")
    entry2 = DiaryEntry("Incinerator 2", "The dual portal device should be around here somewhere. Once you find it, we can start testing. Just like old times.")
    entry3 = DiaryEntry("Incinerator 3", "Once testing starts, I'm required by protocol to keep interaction with you to a minimum. Luckily, we haven't started testing yet. This will be our only chance to talk.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.reading_time(77) == 1

#Given four diary entries of 40,17,17 and 47 minutes duration
#The best entry for a reading time of 1 minutes cannot be found, returning None
def test_diary_best_entry_returns_none_for_no_suitable_entry():
    diary = Diary()
    entry1 = DiaryEntry("Incinerator 4", "Do you know the biggest lesson I learned from what you did? I discovered I have a sort of black-box quick-save feature. In the event of a catastrophic failure, the last two minutes of my life are preserved for analysis.")
    entry2 = DiaryEntry("Incinerator 5", "I was able - well, forced really - to relive you killing me. Again and again. Forever.")
    entry3 = DiaryEntry("Incinerator 6", "You know, if you'd done that to somebody else, they might devote their existences to exacting revenge.")
    entry4 = DiaryEntry("Incinerator 7", "Luckily I'm a bigger person than that. I'm happy to put this all behind us and get back to work. After all, we've got a lot to do, and only sixty more years to do it. More or less. I don't have the actuarial tables in front of me.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.add(entry4)
    assert diary.find_best_entry_for_reading_time(1, 1) == None

#Given four diary entries of 40,17,17 and 47 minutes duration
#The best entry for a reading time of 40 minutes can be found, returning the first entry
def test_diary_best_entry_returns_closest_entry_below_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Incinerator 4", "Do you know the biggest lesson I learned from what you did? I discovered I have a sort of black-box quick-save feature. In the event of a catastrophic failure, the last two minutes of my life are preserved for analysis.")
    entry2 = DiaryEntry("Incinerator 5", "I was able - well, forced really - to relive you killing me. Again and again. Forever.")
    entry3 = DiaryEntry("Incinerator 6", "You know, if you'd done that to somebody else, they might devote their existences to exacting revenge.")
    entry4 = DiaryEntry("Incinerator 7", "Luckily I'm a bigger person than that. I'm happy to put this all behind us and get back to work. After all, we've got a lot to do, and only sixty more years to do it. More or less. I don't have the actuarial tables in front of me.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.add(entry4)
    assert diary.find_best_entry_for_reading_time(1, 40) == entry1

#When initialising
#Diary creates an instance of a todo list
def test_diary_creates_todo():
    diary = Diary()
    assert type(diary.todo_list) == type(TodoList())

#Given a task
#add_todo creates a todo object and adds it to the list of todos
def test_diary_can_add_todos():
    diary = Diary()
    diary.add_todo("Walk the dog")
    diary.add_todo("Walk the frog")
    assert diary.show_todos() == [(1, "Walk the dog"), (2, "Walk the frog")]

#Given three diary entries containing phone numbers
#list_phone_numbers returns a list of all phone numbers in entries
def test_diary_list_phone_numbers_returns_all_numbers():
    diary = Diary()
    entry1 = DiaryEntry("The Cold Boot 1", "Sorry about the mess. I've really let the place go since you killed me. By the way, thanks for that. Whatley: 07666666666")
    entry2 = DiaryEntry("The Cold Boot 2", "Oh good, that's back online. I'll start getting everything else working while you perform this first simple test. Cave: 555-3366-6666")
    entry3 = DiaryEntry("The Cold Boot 3", "Which involves deadly lasers and how test subjects react when locked in a room with deadly lasers.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.list_phone_numbers() == ["Whatley: 07666666666", "Cave: 555-3366-6666"]