import datetime

# создаем список, элементами которого будет кортеж
traffic_money = []


# разделитель для  удобства восприятия
def separator(simbol, count):
    return simbol * count


# функция пополнения  счета
def put_cash(amount_of_money):  # функция пополнения  счета
    amount = input('Введите сумму для пополнения: ')
    while not amount.isdigit():
        amount = input('Пожалуйста, введите число....')

    traffic_money.append(
        ('Поступление средств ' + data, int(amount)))  # добавляет в traffic_money кортеж из 2 элементов
    print(f'Внесена сумма {amount} УЕ')
    input('\nНажмите Enter чтобы продолжить ')


# функция покупки и ее суммы
def buy(amount_of_money):
    balans = sum([trans[1] for trans in traffic_money])
    product_name = input('Введите название продукта: ')
    amount = int(input('Введите сумму покупки: '))
    if amount <= balans:
        traffic_money.append(
            ('Покупка ' + data + ' ' + product_name, -int(amount)))  # добавляет в traffic_money покупки и ее суммы
    else:
        print('Вы превышаете баланс счета, транзакция отменяется...')

    input('\nНажмите Enter чтобы продолжить ')


def history(traffic_money):  # функция истории транзакций
    print("Баланс счета: ", sum([trans[1] for trans in traffic_money]))
    print('История транзакций:')
    for name, amount in traffic_money:
        print(f'      {name}: {amount} УЕ')  # перебор кортежей и вывод их элементов через ":"

    input('\nНажмите Enter чтобы продолжить ')


def show_date():
    return (datetime.date.today().strftime("%d.%m.%Y"))


# if __name__ == '__main__':
#     print(separator('*', 21))


def my_money():
    while True:
        print(separator('*', 21))
        print("Баланс счета: ", sum([trans[1] for trans in traffic_money]))
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(separator('*', 21))

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            put_cash(traffic_money)
        elif choice == '2':
            buy(traffic_money)
        elif choice == '3':
            history(traffic_money)
        elif choice == '4':
            print('До новых встреч...')
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    my_money()
