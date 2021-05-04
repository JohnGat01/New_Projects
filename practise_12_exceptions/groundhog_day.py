# -*- coding: utf-8 -*-
import warnings
from random import randint
# День сурка
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
CARMA = 0
day = 0
file = 'log.txt'
with open(file, 'w', encoding='utf8') as file:
    file.write('')

def one_day():
    file = 'log.txt'
    global CARMA
    global day
    dice = randint(1, 13)
    if dice <= 7:
        CARMA += dice
    elif dice == 8:
        warnings.warn("I'm GOD now!!!!")
        with open(file, 'a', encoding='utf8') as file:
            file.write("I'm GOD now!!!!\n")
    elif dice == 9:
        warnings.warn('Drink is fuuuunnnn!!!')
        with open(file, 'a', encoding='utf8') as file:
            file.write('Drink is fuuuunnnn!!!\n')
    elif dice == 10:
        warnings.warn('Oh I crashed...')
        with open(file, 'a', encoding='utf8') as file:
            file.write('Oh I crashed...\n')
    elif dice == 11:
        warnings.warn('Gluttony day!!!')
        with open(file, 'a', encoding='utf8') as file:
            file.write('Gluttony day!!!\n')
    elif dice == 12:
        warnings.warn('So depressed today......((( ')
        with open(file, 'a', encoding='utf8') as file:
            file.write('So depressed today......((( \n')
    elif dice == 13:
        warnings.warn("I'll kill my self, I'll do it!!! Wiyyyyyy.... shmack")
        with open(file, 'a', encoding='utf8') as file:
            file.write("I'll kill my self, I'll do it!!! Wiyyyyyy.... shmack\n")
    day += 1


while True:
    if ENLIGHTENMENT_CARMA_LEVEL > CARMA:
        warnings.simplefilter("ignore")
        one_day()
        if ENLIGHTENMENT_CARMA_LEVEL <= CARMA:
            print(f'We out of groundhog day for {day} days!!!')
            break
        print(f'My carma - {CARMA}, I need {ENLIGHTENMENT_CARMA_LEVEL-CARMA} more!')
