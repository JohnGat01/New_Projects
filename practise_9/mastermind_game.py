from mastermind_engine import all_answers, input_number, check_number, get_one_answer

print('Игра Быки и Коровы!')
answer = all_answers()
enemy = get_one_answer(answer)
while True:
    print('=' * 15, 'Ход игрока', '=' * 15)
    print("Угадайте число компютера")
    print(enemy)
    number = input_number()
    bulls, cows = check_number(number, enemy)
    print('Быки - ', bulls, 'Коровы - ', cows)
    if bulls == 4:
        print('Вы победили!')
