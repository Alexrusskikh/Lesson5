import Programms
from Programms.use_functions import separator, put_cash, buy, traffic_money
import datetime
import os

def test_separator():
    assert separator('*', 5) == '*****'
    assert separator('Ж', 5) != ';;;;;'

def test_mkdir():
    if not os.path.exists('folder mk'):
        os.mkdir('folder mk')
    assert 'folder mk' in os.listdir()
    if os.path.exists('folder mk'):
        os.rmdir('folder mk')

def test_listdir():
    path = "C:/Users/Alex/PycharmProjects/PS/Lesson5"
    assert isinstance(os.listdir(path), list) == True
    assert isinstance(os.listdir(path), dict) == False


def test_path_exists():
    assert os.path.exists("C:/Users/Alex/PycharmProjects/PS/Lesson5/test_filemanager.py") == True

def test_path_isfile():
    assert os.path.isfile("C:/Users/Alex/PycharmProjects/PS/Lesson5/test_filemanager.py") == True






