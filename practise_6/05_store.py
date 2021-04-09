# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

for stuff in store:
    if stuff == '12345':
        quantity = store['12345'][0]['quantity']
        price = store['12345'][0]['price']
        all_price = price * quantity
        print('Лампа - ', quantity, 'шт', 'общая стоимость -', all_price, 'рублей.')
    elif stuff == '23456':
        quantity1 = store['23456'][0]['quantity']
        price1 = store['23456'][0]['price']
        quantity2 = store['23456'][1]['quantity']
        price2 = store['23456'][1]['price']
        all_price = price1 * quantity1 + quantity2 * price2
        print('Стол - ', quantity1 + quantity2, 'шт', 'общая стоимость -', all_price, 'рублей.')
    elif stuff == '34567':
        quantity1 = store['34567'][0]['quantity']
        price1 = store['34567'][0]['price']
        quantity2 = store['34567'][1]['quantity']
        price2 = store['34567'][1]['price']
        all_price = price1 * quantity1 + quantity2 * price2
        print('Диван - ', quantity1 + quantity2, 'шт', 'общая стоимость -', all_price, 'рублей.')
    elif stuff == '45678':
        quantity1 = store['45678'][0]['quantity']
        price1 = store['45678'][0]['price']
        quantity2 = store['45678'][1]['quantity']
        price2 = store['45678'][1]['price']
        quantity3 = store['45678'][2]['quantity']
        price3 = store['45678'][2]['price']
        all_price = price1 * quantity1 + quantity2 * price2 + quantity3 * price3
        print('Стул - ', quantity1 + quantity2 + quantity3, 'шт', 'общая стоимость -', all_price, 'рублей.')
