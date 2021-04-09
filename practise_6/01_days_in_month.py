# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

if month == 1:
    month = '30'
elif month == 2:
    month = '28'
elif month == 3:
    month = '31'
elif month == 4:
    month = '30'
elif month == 5:
    month = '31'
elif month == 6:
    month = '30'
elif month == 7:
    month = '31'
elif month == 8:
    month = '30'
elif month == 9:
    month = '31'
elif month == 10:
    month = '30'
elif month == 11:
    month = '31'
elif month == 12:
    month = '30'

print('Вы ввели', month)