""" в модуле проводится ручная проверка функций """
import math as M

def filter_odd_num(in_num):
    """    находит четные  числа - True    """
    if (in_num % 2) != 0:
        return False  # если не  четное, т.е. есть остаток  при  делении
    else:
        return True  # если число четное...

def even_odd(x):
    """
    вместо четного числа  возвращает 0, если нет - то аргумент
    """
    if x % 2 == 0:
        return 0
    else:
        return x

def area_of_circle(radius):
    """
    принимает аргументом радиус и вычисляет площадь круга pi*r квадрат
    """
    return round(M.pi, 2) * (radius ** 2)  # округляем  const pi до второго знака после запятой

def square_root(num):
    """
    извлечение квадратного корня от числа
    """
    return round(M.sqrt(num))

def exponentiation(a, n):
    """возведение числа a в степень n
    """
    return round(M.pow(a, n))


def fan_euclid(x, y):
    """евклидова норма вектора msqrt(х * х + у * у)
    """
    return M.hypot(x, y)

if __name__ == '__main__':

    # Применение filter() для удаления нечетных чисел из списка
    numbers = [1, 2, 4, 5, 7, 8, 10, 11, 12]
    out_filter = filter(filter_odd_num, numbers)
    print("Тип объекта out_filter: ", type(out_filter))
    print("Отфильтрованный список: ", list(out_filter))

    # Замена в списке четных чисел на 0
    elements = [1, 2, 3, 4, 5, 6]
    elements_new = list(map(even_odd, elements))
    print(f'Изменный список {elements_new}')

    # обратная сортировка функцией sorted
    num_1 = (15, 3, 5, 7, 9, 11, 42)
    num_2 = sorted(num_1, key=None, reverse=True)
    print(f'Изменный обратный список {num_2}')

    #площад круга
    radius = 3
    print("Площадь круга: ", area_of_circle(radius), 'см квадратных')

    print("Квадратный корень 25: ", M.sqrt(25))

    print("Степень 3 числа 5: ", M.pow(5, 3))

    print("Евклидова норма вектора (3, 4): ", M.hypot(3, 4))