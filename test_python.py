# В модуле написать тесты для встроенных функций
# filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
from Programms.use_functions import separator
from any_function import filter_odd_num, even_odd, area_of_circle, square_root, \
    exponentiation, fan_euclid


def test_filter_odd_num():
    """при аргументе 2 получим True, при 3 - False"""
    assert filter_odd_num(2) == True
    assert filter_odd_num(3) == False

def test_filter():
    """
    тест встроенной функции filter
    """
    numbers = [1, 2, 4, 5, 7, 8, 10, 11, 12]
    assert list(filter(filter_odd_num, numbers)) == [2, 4, 8, 10, 12]

def test_even_odd():
    """ замена четного числа  на 0 """
    assert even_odd(2) == 0
    assert even_odd(3) != 0

def test_map():
    """ тест встроенной функции map"""
    elements = [1, 2, 3, 4]
    assert list(map(even_odd, elements)) == [1, 0, 3, 0]

# тест встроенной функции sorted
def test_sorted():
    num_1 = (15, 3, 5, 7, 9, 11, 42)
    assert sorted(num_1, key=None, reverse=True) == [42, 15, 11, 9, 7, 5, 3]
    num_2 = sorted(num_1, key=None, reverse=True)
    assert num_2[0] > num_2[-1]

def test_area_of_circle():
    """тест  функции  с константой pi, площадь  круга  """
    assert area_of_circle(3) == 28.26

#
def test_square_root():
    """тест  функции  sqrt, корень  квадратный  из числа
    """
    assert square_root(25) == 5

def test_exponentiation():
    """
    тест  функции  pow
    """
    assert exponentiation(5, 3) == 125

def test_fan_euclid():
    """
    евклидова норма вектора msqrt(х * х + у * у)
    """
    assert fan_euclid(3, 4) == 5

#
def test_separator():
    """
    разделитель
    """
    assert separator('*', 5) == '*****'
    assert separator('*', 5) != '/////'
    assert separator('*', 5) != '/////*****'