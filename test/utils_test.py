import pytest
from utils import *

def test_get_data2():
    assert type(get_data2()) == list
    assert len(get_data2()) == 91
    assert get_data2()[0]['day_week'] == 'пн'


def test_get_lesson_by_day():
    assert type(get_lesson_by_day('пн')) == list
    assert len(get_lesson_by_day('пн')) == 14


def test_search_by_word():
    assert type(search_by_word('пн')) == list
    assert len(search_by_word('пн')) == 14

def test_get_lesson():
    assert type(get_lesson('Теория тепловых процессов')) == list