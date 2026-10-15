from lib.diary_entry import *

#Given a title and contents
#Diary entry can be stored
def test_diary_entry_stores_entry():
    entry = DiaryEntry("Title 1", "This is text")
    assert entry.title == "Title 1"
    assert entry.contents == "This is text"

#Given an empty entry
#Count words returns the number of words in the contents of that entry
def test_entry_count_words_returns_zero_for_empty():
    entry = DiaryEntry("Title 1", "")
    assert entry.count_words() == 0

#Given a non-empty entry
#Count words returns the number of words in the contents of that entry
def test_entry_count_words_returns_words_in_entry():
    entry = DiaryEntry("Title 1", "This is text")
    assert entry.count_words() == 3

#Given a non-empty entry
#reading time returns number of minutes taken to read entry
def test_entry_time_returns_time_to_read_entry():
    entry = DiaryEntry("Title 1", "This is text")
    assert entry.reading_time(1) == 3

#When reading_chunk is called with values to read whole contents
#Returns string with whole contents
def test_diary_entry_reading_chunk_returns_10_words_for_10_wpm_1_minute():
    entry = DiaryEntry("Questions to Cave", "What was in that phonebook of a contract I signed?")
    result = entry.reading_chunk(10,1)
    assert result == "What was in that phonebook of a contract I signed?"

#When reading_chunk is called twice whilst text is not complete
#Second call returns text starting from the point the first call ended
def test_diary_entry_reading_chunk_continues_along_text_after_sequential_calls():
    entry = DiaryEntry("Introduction", "Greetings, friend. I'm Cave Johnson, CEO of Aperture Science. You might know us as a vital participant in the 1968 senate hearings on missing astronauts. And you've most likely used one of the many products we invented, but that other people have somehow managed to steal from us. Black Mesa can eat my bankrupt-...")
    entry.reading_chunk(2,1)
    result = entry.reading_chunk(3,1)
    assert result == "I'm Cave Johnson,"

#When reading_chunk is called after a previous call has finished the text
#Returns text from start of contents
def test_diary_entry_reading_chunk_continues_from_start_when_called_after_finishing_text():
    entry = DiaryEntry("Asbestos Part Two","Let us know if you feel a shortness of breath, a persistant dry cough or your heart stopping. Because that's not part of the test. That's asbestos")
    entry.reading_chunk(25,1)
    entry.reading_chunk(3,1)
    result = entry.reading_chunk(10,1)
    assert result == "Let us know if you feel a shortness of breath,"

#When reading chunk is called after finishing on the exact last word
#Returns text from start of contents
def test_diary_entry_reading_chunk_continues_from_start_when_called_after_exactly_last_word():
    entry = DiaryEntry("Asbestos Part Two","Let us know if you feel a shortness of breath, a persistant dry cough or your heart stopping. Because that's not part of the test. That's asbestos")
    entry.reading_chunk(25,1)
    entry.reading_chunk(2,1)
    result = entry.reading_chunk(10,1)
    assert result == "Let us know if you feel a shortness of breath,"

#Given a diary entry containing phone numbers
#fetch_phone_numbers returns a list of all phone numbers in entry
def test_diary_entry_fetch_phone_number_returns_number():
    entry1 = DiaryEntry("The Cold Boot 1", "Sorry about the mess. I've really let the place go since you killed me. By the way, thanks for that. Whatley: 07666666666")
    entry2 = DiaryEntry("The Cold Boot 2", "Oh good, that's back online. I'll start getting everything else working while you perform this first simple test. Cave: 555-3366-6666")
    entry3 = DiaryEntry("The Cold Boot 3", "Which involves deadly lasers and how test subjects react when locked in a room with deadly lasers.")
    
    assert entry1.fetch_phone_number() == "Whatley: 07666666666"
    assert entry2.fetch_phone_number() == "Cave: 555-3366-6666"
    assert entry3.fetch_phone_number() == None   