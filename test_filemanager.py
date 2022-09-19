import Programms
from Programms.use_functions import separator, put_cash, data, buy, traffic_money
import datetime
import os


def test_separator():
    assert separator('*', 5) == '*****'

def test_mkdir():
    os.mkdir('folder mk')
    assert 'folder mk' in os.listdir()
    os.rmdir('folder mk')

def test_listdir():
    assert os.listdir("C:/Users/Alex/PycharmProjects/PS/Lesson5")

def test_path_exists():
    assert os.path.exists("C:/Users/Alex/PycharmProjects/PS/Lesson5/test_filemanager.py") == True

def test_path_isfile():
    assert os.path.isfile("C:/Users/Alex/PycharmProjects/PS/Lesson5/test_filemanager.py") == True

def test_environ():
    assert os.environ

def test_getcwd():
    assert os.getcwd()




