# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
BRUCE_WILLIS = 42
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as exs:
    print(f'Ошибка значения - {exs}, введите число больше 5 символов')
except IndexError as exs:
    print(f'Ошибка ввода - {exs}, введите число больше 5 символов')
except Exception as exs:
    print(f'Произошла неожиданная ошибка - {exs}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
