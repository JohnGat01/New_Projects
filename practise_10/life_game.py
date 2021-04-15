from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 50
        self.IQ = 80
        self.houses = 0

    def __str__(self):
        return "I'm {}, my fullness is {}, I have {} food, I have {}$,my IQ is {}, I have {} houses that costs {}$"\
            .format(self.name, self.fullness, self.food, self.money, self.IQ, self.houses, self.houses*20000)

    def eat(self):
        if self.food > 10:
            print("I ate")
            self.fullness += 10
            self.food -= 10
        else:
            print("I don't have food...")

    def go_work(self):
        print("{} go work".format(self.name))
        if self.IQ >= 500:
            self.money += 200
        elif self.IQ >= 400:
            self.money += 150
        elif self.IQ >= 300:
            self.money += 100
        elif self.IQ >= 200:
            self.money += 75
        elif self.IQ < 200:
            self.money += 50
        self.fullness -= 20
        if self.IQ < 500:
            self.IQ += 1

    def buy_food(self):
        print("{} go to shop".format(self.name))
        self.money -= 50
        self.food += 30

    def read_books(self):
        print("{} reading books".format(self.name))
        self.fullness -= 10
        if self.IQ < 500:
            self.IQ += 2

    def act_antons(self):
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()

        elif self.money <= 100:
            self.go_work()

        elif self.food <= 20:
            self.buy_food()

        else:
            if dice == 1:
                self.go_work()
            if dice == 2:
                self.read_books()

    def act_my(self):
        if self.money >= 20200:
            self.houses += 1
            self.money -= 20000

        if self.fullness <= 20:
            self.eat()
            self.money += self.houses * 30

        elif self.money <= 100:
            self.go_work()
            self.money += self.houses * 30

        elif self.food <= 20:
            self.buy_food()
            self.money += self.houses * 30

        else:
            self.go_work()
            self.money += self.houses * 30


antons_son = Man(name="Anton's son")
my_son = Man(name="My son")
for day in range(366 * 10):
    if antons_son.fullness <= 0:
        print("{} dead on {} day of life...".format(antons_son.name, day))
        break
    cprint('=============== Day {} ==============='.format(day), color='yellow')
    my_son.act_my()
    antons_son.act_antons()
    cprint(my_son, color='cyan')
    cprint(antons_son, color='blue')
