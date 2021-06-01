# -*- coding: utf-8 -*-
import csv
import os
import time
from threading import Thread
# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
FILES = []

SECID_VOLATILITY = {}

TICKER = []
MAX_VALUES = []
MIN_VALUES = []
ZERO_VALUES = []

path = '/Users/sasha/Documents/New_Projects/practise_12_multiprocesing/trades/'
file_list = os.listdir(path)

for file_name in file_list:
    FILES.append(file_name)


def time_track(func):
    def surrogate(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed = round(end_time - start_time, 4)
        print(f'Function was working {elapsed} seconds.')
        return result
    return surrogate

# def last_4chars(x):
#     return(x[-8:])


class Main(Thread):

    def __init__(self, file):
        super(Main, self).__init__()
        self.file = file

    def run(self):
        if self.file:
            with open(os.path.join('/Users/sasha/Documents/New_Projects/practise_12_multiprocesing/trades/'
                                   + self.file), 'r', encoding='utf8') as trade:
                reader = csv.reader(trade, delimiter=',')
                secid = []
                tradetime = []
                prices = []
                quantity = []
                for row in reader:
                    if row[0] == 'SECID':
                        continue
                    secid.append(row[0])
                    tradetime.append(row[1])
                    prices.append(row[2])
                    quantity.append(row[3])
                price = map(float, prices)
                prices = list(price)
                max_price = max(prices)
                min_price = min(prices)
                average_price = round((max_price + min_price) / 2, 2)
                volatility = round((max_price - min_price) / average_price * 100, 2)
                SECID_VOLATILITY[secid[0]] = volatility


# def main(path):
#     file_list = os.listdir(path)
#     file_listed = sorted(file_list, key=last_4chars)
#     for file in file_listed:
#         with open(os.path.join('/Users/sasha/Documents/New_Projects/practise_12_multiprocesing/trades/' + file), 'r',
#                   encoding='utf8') as trade:
#             reader = csv.reader(trade, delimiter=',')
#             secid = []
#             tradetime = []
#             prices = []
#             quantity = []
#             for row in reader:
#                 if row[0] == 'SECID':
#                     continue
#                 secid.append(row[0])
#                 tradetime.append(row[1])
#                 prices.append(row[2])
#                 quantity.append(row[3])
#             price = map(float, prices)
#             prices = list(price)
#             max_price = max(prices)
#             min_price = min(prices)
#             average_price = round((max_price + min_price)/2, 2)
#             volatility = round((max_price - min_price)/average_price * 100, 2)
#             yield secid[0], volatility

for file_name in file_list:
    FILES.append(file_name)

@time_track
def func():

    sizers = [Main(file=file) for file in FILES]
    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()

    dict_volatility = {}
    dict_zero_volatility = {}
    for secid, volatility in SECID_VOLATILITY.items():
        if volatility >= 0.1:
            dict_volatility[secid] = volatility
        else:
            dict_zero_volatility[secid] = volatility

    sorted_dict = {k: v for k, v in sorted(dict_volatility.items(), key=lambda item: item[1], reverse=True)}
    sorted_zero_dict = {k: v for k, v in sorted(dict_zero_volatility.items(), key=lambda item: item[0], reverse=False)}
    zero_list = list(sorted_zero_dict.items())
    my_list = list(sorted_dict.items())
    MAX_VALUES.extend([my_list[0], my_list[1], my_list[2]])
    MIN_VALUES.extend([my_list[-1], my_list[-2], my_list[-3]])
    ZERO_VALUES.extend(zero_list)







if __name__ == '__main__':
    func()
    print(f' Максимальная волатильность:\n\t{MAX_VALUES[0][0]} - {MAX_VALUES[0][1]}%\n\t'
          f'{MAX_VALUES[1][0]} - {MAX_VALUES[1][1]}%\n\t{MAX_VALUES[2][0]} - {MAX_VALUES[2][1]}%')
    print(f' Минимальная волатильность:\n\t{MIN_VALUES[0][0]} - {MIN_VALUES[0][1]}%\n\t'
          f'{MIN_VALUES[1][0]} - {MIN_VALUES[1][1]}%\n\t{MIN_VALUES[2][0]} - {MIN_VALUES[2][1]}%')
    print(f' Нулевая волатильность:\n\t{list(item for sublist in ZERO_VALUES for item in sublist)}%')
