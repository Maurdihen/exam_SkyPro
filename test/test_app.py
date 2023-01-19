import pytest
from app import app

def test_search_page():
    params = {"s": 'пн'}
    response = app.test_client().get('/search', query_string=params)
    assert response.status_code == 200


def test_main_page():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_list_lesson():
    response = app.test_client().get('/list')
    assert response.status_code == 200
