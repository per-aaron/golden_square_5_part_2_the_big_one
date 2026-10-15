from lib.diary import *

#Given a Diary with no entries
#An empty list is returned by all()
def test_diary_starts_empty_list():
    diary = Diary()
    assert diary.all() == []

#Given an empty diary
#count_words returns 0
def test_count_words_returns_zero_on_empty_diary():
    diary = Diary()
    assert diary.count_words() == 0

#Given an empty diary
#reading_time returns 0
def test_reading_time_returns_zero_on_empty_diary():
    diary = Diary()
    assert diary.reading_time(1) == 0

