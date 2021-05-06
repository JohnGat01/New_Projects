# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
from termcolor import cprint
import time

start_time = time.time()

file_name = 'registrations.txt'
good_log = 'registrations_good.log'
bad_log = 'registrations_bad.log'
errors = 0

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def clear_logs(good_log, bad_log):
    with open(good_log, 'w') as log:
        log.write('')
    with open(bad_log, 'w') as log:
        log.write('')


clear_logs(good_log, bad_log)


def check(line):
    line_active = line.split()
    name = line_active[0]
    mail = line_active[1]
    age = line_active[2]
    if name.isalpha() is False:
        raise NotNameError()
    elif '@' not in mail or '.' not in mail:
        raise NotEmailError()
    elif int(age) < 10 or int(age) > 99:
        raise ValueError
    else:
        with open(good_log, 'a', encoding='utf8') as log:
            log.write(f'{line}')


with open(file_name, 'r', encoding='utf8') as file:
    for line in file:
        try:
            check(line=line)
        except IndexError as exs:
            # print(f"Have error in line '{line[:-1]}', error - {exs}")
            errors += 1
            with open(bad_log, 'a', encoding='utf8') as log:
                log.write(f'{line[:-1]} [global data error]\n')
        except NotNameError:
            # print(f"Have NotNameError in line '{line[:-1]}', error - name doesn't have only letters")
            errors += 1
            with open(bad_log, 'a', encoding='utf8') as log:
                log.write(f'{line}')
        except NotEmailError:
            # print(f"Have NotEmailError in line '{line[:-1]}', error - email doesn't have '@' or '.'")
            errors += 1
            with open(bad_log, 'a', encoding='utf8') as log:
                log.write(f'{line}')
        except ValueError:
            # print(f"Have ValueError in line '{line[:-1]}', error - age is less than 10 or more than 99")
            errors += 1
            with open(bad_log, 'a', encoding='utf8') as log:
                log.write(f'{line}')

cprint(f"In file {file_name} we have - {errors} errors", color='yellow')
print('\n', ''"========== %s seconds ==========" % (time.time() - start_time))
