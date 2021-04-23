from random import randint
from termcolor import cprint


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 50
        self.purity = 100

    def __str__(self):
        return 'In fridge we have {} food and {} cat food, purity in house is {}, in nightstand we have {}$'.format(
            self.food, self.cat_food, self.purity, self.money)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.IQ = 80
        self.house = None
        self.happiness = 100

    def __str__(self):
        return "I'm {}, my fullness is {},my IQ is {}, my happiness - {}".format(
            self.name, self.fullness, self.IQ, self.happiness)

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} go into house!!!'.format(self.name))

    def eat(self):
        if self.house.food >= 30:
            print("{} ate".format(self.name))
            if self.happiness <= 90:
                self.happiness += 10

            if self.fullness < 50:
                self.house.food -= 30
                self.fullness += 30
            elif self.fullness < 30:
                self.house.food -= 20
                self.fullness += 20
            else:
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
            self.house.money += 100
        if self.IQ < 200:
            self.IQ += 1
        self.fullness -= 10
        self.happiness -= 10

    def read_books(self):
        print("{} reading books".format(self.name))
        self.fullness -= 10
        if self.IQ < 199:
            self.IQ += 2
        if self.happiness <= 95:
            self.happiness += 5

    def play_poker(self):
        dice = randint(1, 100)
        if dice < 33:
            self.house.money -= 50
            self.happiness -= 10
            print(f'{self.name} played poker and lost money... he is sad')
        elif 33 > dice < 66:
            self.house.money += 50
            if self.happiness <= 95:
                self.happiness += 5
            print(f'{self.name} played poker and win some money! He is quite happy')
        else:
            if self.happiness <= 95:
                self.happiness += 15
            self.house.money += 250
            print(f'{self.name} played poker and won tournament!!! He feels like Elon Musk!')

    def act(self):
        dice = randint(1, 2)
        if self.fullness <= 50:
            self.eat()
        elif self.house.money <= 100:
            self.go_work()
        elif dice == 1:
            self.read_books()
        else:
            self.play_poker()

        if self.house.purity <= -20:
            self.happiness -= 10


class Women:

    charity_foundation = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.IQ = 80
        self.house = None
        self.happiness = 100

    def __str__(self):
        return "I'm {}, my fullness is {},my IQ is {}, my happiness - {}".format(
            self.name, self.fullness, self.IQ, self.happiness)

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} go into house!!!'.format(self.name))

    def eat(self):
        if self.house.food >= 30:
            print("{} ate".format(self.name))
            if self.happiness <= 90:
                self.happiness += 10

            if self.fullness < 50:
                self.house.food -= 30
                self.fullness += 30
            elif self.fullness < 30:
                self.house.food -= 20
                self.fullness += 20
            else:
                self.fullness += 10
                self.house.food -= 10
        else:
            print("I don't have food...")

    def house_food(self):
        print("{} go to shop".format(self.name))
        self.house.money -= 50
        self.house.food += 30
        if self.house.cat_food <= 100:
            print(f"{self.name} bought cat food")
            self.house.money -= 50
            self.house.cat_food += 50
        self.happiness -= 10

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
        self.happiness -= 5

    def save_earth(self):
        charity_fee = 350
        self.house.money -= charity_fee
        print(f'{self.name} is saving the world! She gave to charity {charity_fee}$')
        Women.charity_foundation += charity_fee
        if self.happiness <= 70:
            self.happiness += 30

    def read_books(self):
        print("{} reading books".format(self.name))
        self.fullness -= 10
        if self.IQ < 199:
            self.IQ += 2

    def act(self):

        if self.fullness <= 50:
            self.eat()

        elif self.house.food <= 50:
            self.house_food()

        elif self.house.purity <= 0:
            self.clean_house()

        elif self.house.money >= 1000:
            self.save_earth()

        else:
            self.read_books()

        if self.house.purity <= -20:
            self.happiness -= 10


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


me = Man(name="Sasha")
my_wife = Women(name="Oksana")
cat_1 = Cat(name="Shashlichok")
cat_2 = Cat(name='Kukuryza')
cat_3 = Cat(name='Moloko')

our_sweet_home = House()

me.go_into_the_house(house=our_sweet_home)
my_wife.go_into_the_house(house=our_sweet_home)
cat_1.go_into_the_house(house=our_sweet_home)
cat_2.go_into_the_house(house=our_sweet_home)
cat_3.go_into_the_house(house=our_sweet_home)

for day in range(365):
    if my_wife.fullness <= 0:
        print("{} dead on {} day of life...".format(my_wife.name, day))
        break
    if me.fullness <= 0:
        print("{} dead on {} day of life...".format(my_wife.name, day))
        break
    if cat_1.fullness <= 0:
        print("{} is dead...".format(cat_1.name, day))
        break
    if cat_2.fullness <= 0:
        print("{} is dead...".format(cat_1.name, day))
        break
    if cat_3.fullness <= 0:
        print("{} is dead...".format(cat_1.name, day))
        break

    cprint(f'=============== Day {day} ===============', color='yellow')
    me.act()
    my_wife.act()
    cat_1.act()
    cat_2.act()
    cat_3.act()
    cprint(me, color='cyan')
    cprint(my_wife, color='blue')
    cprint(cat_1, color='yellow')
    cprint(cat_2, color='yellow')
    cprint(cat_3, color='yellow')
    print(our_sweet_home)

print(f'{my_wife.name} charity to save the world is {Women.charity_foundation}$')
