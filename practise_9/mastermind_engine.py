import random


def all_answers():
    answers = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        if len(set(map(int, tmp))) == 4:
            answers.append(list(map(int, tmp)))
    return answers


def get_one_answer(answers):
    number = random.choice(answers)
    return number


def input_number():
    while True:
        number = input('Введите 4 неповторяющиеся цифры: ')
        if len(number) != 4:
            continue
        number = list(map(int, number))
        if len(set(number)) == 4:
            break
    return number


def check_number(number, true_number):
    bulls, cows = 0, 0
    for i, num in enumerate(number):
        if num in true_number:
            if number[i] == true_number[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows
