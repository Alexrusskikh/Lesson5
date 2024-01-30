"""Консольный файловый менеджер

"""
import platform
import os
from collections import namedtuple
import sys
import shutil
from Programms.use_functions import separator
from Programms.use_functions import my_money
from Programms.use_functions import show_date

print(f'Текущая дата: {show_date()}')
print(separator('*', 20))
print("Меню: ")

while True:
    print('0. в какой я директории?')
    print('1. создать папку/файл')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. просмотреть только файлы')
    print('6. просмотреть только папки')
    print('7. просмотр информации об операционной системе')
    print('8. информация о файле')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')
    print(separator('*', 20))

    choice = input('Выберите пункт меню: ')
    print(separator('*', 20))

    if choice == '0':
        print("Текущая деректория:", os.getcwd())

    elif choice == '1':
        new_folder = input('Создать папку в текущей директории (введите название): ')
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
        else:
            print('Такая папка существует!')

    elif choice == '2':
        del_folder = input('Удалить папку (введите путь): ')
        if os.path.exists(del_folder):
            os.rmdir(del_folder)
        else:
            print('Такой папки нет!')
    elif choice == '3':
        print("Текущая деректория:", os.getcwd())
        review_dir = os.listdir()
        for el in review_dir:
            print(el)
        new_round = "да"
        while new_round == "да" or new_round == "Да":
            exist_path_copy = input('Введите путь исходного файла: ')
            if os.path.exists(exist_path_copy):
                new_path_copy = input('Введите путь нового файла: ')
                if os.path.exists(new_path_copy):
                    print('Такой файл ЕСТЬ!')
                    break
                shutil.copy(exist_path_copy, new_path_copy)
                print('Операция совершена!')
            else:
                print('Такого файла НЕТ!')
            new_round = input("Хотите начать заново? (Да-Нет): ")
            new_round = new_round.lower()
    elif choice == '4':
        print(os.listdir())

    elif choice == '5':
        print("Текущая деректория:", os.getcwd())
        all_objects = os.listdir()
        print('Текущая папка содержит файлы: ')
        for object in all_objects:
            if os.path.isfile(object):
                print(object)

    elif choice == '6':
        print("Текущая деректория:", os.getcwd())
        all_objects = os.listdir()
        print('Текущая папка содержит папки: ')
        for object in all_objects:
            if os.path.isdir(object):
                print(object)

    elif choice == '7':
        platform_info = platform.uname()
        platform_info_dict = platform_info._asdict()
        num = 1
        for k, v in platform_info_dict.items():
            print(f' {num}. {k} = {v}')
            num += 1

    elif choice == '8':
        size_file = input('Введите путь к нужному файлу: ')
        print('Размер файла: ', os.stat(size_file).st_size)
    elif choice == '9':
        from Programms import victory
    elif choice == '10':
        my_money()
    elif choice == '11':
        print ('Текущая папка: ', os.getcwd())
        new_path = input('Перейти в: ')
        os.chdir(new_path)
        print('Совершен переход: ', os.getcwd())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
    print(separator('*', 20))
