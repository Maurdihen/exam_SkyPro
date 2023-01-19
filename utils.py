import json
import logging

logging.basicConfig(level=logging.INFO)

def get_data2():
    """
    Получает всю информацию из Json и конвертирует его в удобный для питона формат
    """
    with open('data/data2.json', 'r', encoding='utf-8') as data:
        data =  json.load(data)
        l = []
        while len(data) > 0:
            for j in ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']:
                for i in data:
                    if i['day_week'] == j:
                        l.append(i)
                        del data[data.index(i)]
                        break
        return l

def get_lesson_by_day(day):
    """
    Принемает аргументом день недели и возврашает список из уроков в этот день недели
    """
    return [i for i in get_data2() if i['day_week'] == day]

def search_by_word(word):
    """
    Аргументом принемает слово которое может быть именем учителя названием дисциплины днём недели и возвращает список уроков по данным нужен для оброботки запроса /search
    """
    return [i for i in get_data2() if word.lower() == i['day_week'].lower() or word.lower() == i['discipline'].lower() or word.lower() in i['teacher'].lower()]

def get_lesson(less):
    """
    Аргументом принемает в себя название дисциплины возвращает все данные все уроки по этой дисциплине
    """
    return [i for i in get_data2() if i['discipline'] == less]

def get_teachers():
    """
    Получает список всех учителей
    """
    techers = [i['teacher'] for i in get_data2()]
    techers = set(techers)
    return techers