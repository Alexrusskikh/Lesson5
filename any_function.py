import math as M

# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]


# функция, которая фильтрует нечетные числа
def filter_odd_num(in_num):
    if (in_num % 2) != 0:
        return False
    else:
        return True


# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))


# замена четных  числе на 0
def even_odd(x):
    if x % 2 == 0:
        return 0
    else:
        return x


# функция list
elements = [1, 2, 3, 4]
elements_new = list(map(even_odd, elements))
print(f'Изменный список {elements_new}')

# обратная сортировка функцией sorted
num_1 = (15, 3, 5, 7, 9, 11, 42)
num_2 = sorted(num_1, key=None, reverse=True)
print(f'Изменный обратный список {num_2}')


# функция с константой pi
def area_of_circle(radius):
    return round(M.pi, 2) * (radius ** 2)  # округляем  const pi до второго знака после запятой


# print("Площадь круга: ", area_of_circle(3))

# извлечение квадратного корня
def square_root(num):
    return round(M.sqrt(num))


# print("Квадратный корень 25: ", M.sqrt(25))

# возведение числа  в степень
def exponentiation(a, n):
    return round(M.pow(a, n))


# print("Степень 3 числа 5: ", M.pow(5, 3))

# евклидова норма вектора msqrt(х * х + у * у)
def fan_euclid(x, y):
    return M.hypot(x, y)


# print("евклидова норма вектора (3, 4): ", M.hypot(3, 4))


