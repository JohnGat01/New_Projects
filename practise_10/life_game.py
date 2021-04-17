from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.IQ = 80
        self.house = None

    def __str__(self):
        return "I'm {}, my fullness is {},my IQ is {}".format(self.name, self.fullness, self.IQ)

    def eat(self):
        if self.house.food >= 10:
            print("{} ate".format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print("I don't have food...")

    def go_work(self):
        print("{} go work".format(self.name))
        if self.IQ >= 200:
            self.house.money += 300
        elif self.IQ >= 175:
            self.house.money += 250
        elif self.IQ >= 150:
            self.house.money += 200
        elif self.IQ > 100:
            self.house.money += 150
        elif self.IQ < 100:
            self.house.money += 75
        self.fullness -= 20
        if self.IQ < 200:
            self.IQ += 1

    def buy_food(self):
        print("{} go to shop".format(self.name))
        self.house.money -= 50
        self.house.food += 30

    def buy_cat_food(self):
        print("{} bought cat food".format(self.name))
        self.house.money -= 50
        self.house.cat_food += 50

    def read_books(self):
        print("{} reading books".format(self.name))
        self.fullness -= 10
        if self.IQ < 199:
            self.IQ += 2

    def clean_house(self):
        print('{} cleaned the house'.format(self.name))
        if self.house.purity == -20:
            self.fullness -= 30
            self.house.purity += 120
        elif self.house.purity == -10:
            self.fullness -= 25
            self.house.purity += 110
        else:
            self.fullness -= 20
            self.house.purity += 100

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} go into house!!!'.format(self.name))

    def act_my_wife(self):
        dice = randint(1, 2)
        if self.fullness <= 50:
            self.eat()

        elif self.house.food <= 50:
            self.buy_food()
            if self.house.cat_food <= 50:
                self.buy_cat_food()

        elif self.house.purity <= 0:
            self.clean_house()

        else:
            if dice == 1:
                self.go_work()
            if dice == 2:
                self.read_books()

    def act_me(self):
        dice = randint(1, 4)
        if self.fullness <= 50:
            self.eat()

        elif self.house.money <= 100:
            self.go_work()

        elif dice == 1:
            self.read_books()

        else:
            self.go_work()

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return "I'm {}, my fullness is {}".format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food > 10:
            self.house.cat_food -= 10
            self.fullness += 20
            print('{} ate'.format(self.name))
        else:
            print('MMMEEEEAAAAAAAWWWW!!')

    def playing(self):
        print('{} plays :)'.format(self.name))
        self.fullness -= 10
        self.house.purity -= 5

    def sleep(self):
        print('{} is sleeping murrr :)'.format(self.name))
        self.fullness -= 5

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 5
        print('{} go into house, murrrrr!!!'.format(self.name))

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 20:
            self.eat()

        elif dice == 1:
            self.playing()

        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 50
        self.purity = 100

    def __str__(self):
        return 'In fridge we have {} food and {} cat food, purity in house is {}, in bank we have {}$'.format(
            self.food, self.cat_food, self.purity,self.money)


my_wife = Man(name="Oksana")
me = Man(name="Sasha")
cat_1 = Cat(name="Shashlichok")
cat_2 = Cat(name='Kukuryza')
cat_3 = Cat(name='Moloko')



our_sweet_home = House()
me.go_into_the_house(house=our_sweet_home)
my_wife.go_into_the_house(house=our_sweet_home)
cat_1.go_into_the_house(house=our_sweet_home)
cat_2.go_into_the_house(house=our_sweet_home)
cat_3.go_into_the_house(house=our_sweet_home)

for day in range(366 * 3):
    if my_wife.fullness <= 0:
        print("{} dead on {} day of life...".format(my_wife.name, day))
        break
    if me.fullness <= 0:
        print("{} dead on {} day of life...".format(my_wife.name, day))
        break
    if cat_1.fullness <= 0:
        print("{} is dead...".format(cat_1.name, day))
    if cat_2.fullness <= 0:
        print("{} is dead...".format(cat_1.name, day))
    if cat_3.fullness <= 0:
        print("{} is dead...".format(cat_1.name, day))
    cprint('=============== Day {} ==============='.format(day), color='yellow')
    me.act_me()
    my_wife.act_my_wife()
    cat_1.act()
    cat_2.act()
    cat_3.act()
    cprint(me, color='cyan')
    cprint(my_wife, color='blue')
    cprint(cat_1, color='yellow')
    cprint(cat_2, color='yellow')
    cprint(cat_3, color='yellow')
    print(our_sweet_home)
