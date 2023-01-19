from flask import Flask, render_template, request
from utils import *
import logging

# logging.basicConfig(level=logging.INFO, filename='logs.log', format='%(asctime)s [%(levelname)s] %(message)s')


new_logger = logging.getLogger()
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler = logging.FileHandler("logs.log")
file_handler.setFormatter(formatter_one)
new_logger.addHandler(file_handler)

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def main_page():
    new_logger.info('Пользователь загрузил главную страничку')
    """
    Вьюшка главной страницы
    """
    days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    day = []
    datas = get_data2()
    for i in days:
        day.append(get_lesson_by_day(i))
    return render_template('index.html', datas=datas)

@app.route('/search')
def search_page():
    new_logger.info('Пользователь что ищет на сайте')
    """
    Вьюшка для поиска
    """
    s = request.args.get('s')
    serch = search_by_word(s)
    return render_template('search.html', serch=serch)

@app.route('/list')
def list_lesson():
    new_logger.info('Пользователь загрузил список уроков')
    """
    Вьюшка для вывода списка предметов
    """
    lesson = get_data2()
    lesson = [i['discipline'] for i in lesson]
    lesson = set(lesson)
    return render_template('lesson.html', lesson=lesson)

@app.route('/lesson/<less>')
def lesson_page(less):
    new_logger.info('Пользоваетль вывел список предметов с данными')
    """
    Вьюшка для вывода списка предметов с данными
    """
    lesson = get_lesson(less)
    return render_template('search.html', serch=lesson)

@app.route('/teachers')
def teachers_page():
    new_logger.info('Пользоваетль вывел список учителей')
    teachers = get_teachers()
    return render_template('teacher.html', teachers=teachers)


if __name__ == '__main__':
    app.run()