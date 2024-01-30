# В модуле написать тесты для встроенных функций
# filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
from Programms.use_functions import separator
from any_function import filter_odd_num, even_odd, area_of_circle, square_root,\
    exponentiation, fan_euclid




# тест встроенной функции filter
def test_filter():
    numbers = [1, 2, 4, 5, 7, 8, 10, 11]
    assert list(filter(filter_odd_num, numbers)) == [2, 4, 8, 10]


# тест встроенной функции map
def test_map():
    elements = [1, 2, 3, 4]
    assert list(map(even_odd, elements)) == [1, 0, 3, 0]


# тест встроенной функции sorted
def test_sorted():
    num_1 = (15, 3, 5, 7, 9, 11, 42)
    assert sorted(num_1, key=None, reverse=True) == [42, 15, 11, 9, 7, 5, 3]


# тест  функции  с константой pi
def test_area_of_circle():
    assert area_of_circle(3) == 28.26


# тест  функции  sqrt
def test_square_root():
    assert square_root(25) == 5


# тест  функции  pow
def test_exponentiation():
    assert exponentiation(5, 3) == 125


# евклидова норма вектора msqrt(х * х + у * у)
def test_fan_euclid():
    assert fan_euclid(3, 4) == 5

# разделитель
def test_separator():
    assert separator('*', 5) == '*****'






