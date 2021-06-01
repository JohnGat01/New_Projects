import csv
import os
import time


SECID_VOLATILITY = {}

TICKER = []
MAX_VALUES = []
MIN_VALUES = []
ZERO_VALUES = []

path = '/Users/sasha/Documents/New_Projects/practise_12_multiprocesing/trades/'
file_list = os.listdir(path)

def time_track(func):
    def surrogate(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed = round(end_time - start_time, 4)
        print(f'Function was working {elapsed} seconds.')
        return result
    return surrogate


def last_4chars(x):
    return(x[-8:])


def main(path):
    file_list = os.listdir(path)
    file_listed = sorted(file_list, key=last_4chars)
    for file in file_listed:
        with open(os.path.join('/Users/sasha/Documents/New_Projects/practise_12_multiprocesing/trades/' + file), 'r',
                  encoding='utf8') as trade:
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
            average_price = round((max_price + min_price)/2, 2)
            volatility = round((max_price - min_price)/average_price * 100, 2)
            yield secid[0], volatility

@time_track
def func():
    dict_volatility = {}
    dict_zero_volatility = {}
    for secid, volatility in main(path=path):
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