from termcolor import cprint


class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return 'In {} warehouse {} KG goods.'.format(self.name, self.content)

    def set_road_out(self, road):
        pass

    def truck_arrived(self, truck):
        pass

    def get_next_truck(self):
        pass

    def truck_ready(self, truck):
        pass

    def act(self):
        pass


class Vehicle:
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} has {} fuel'.format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000


class Truck(Vehicle):

    def __init__(self, model, body_space):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 80
        self.place = None
        self.dictance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + ' {} cargo'.format(self.cargo)

    def ride(self):
        if self.dictance_to_target >= self.velocity:
            self.dictance_to_target -= self.velocity
        print('{} is going on the road, {} km left'.format(self.model, self.dictance_to_target))

    def go_to(self, road):
        self.place = road
        self.dictance_to_target = road.distance
        print('{} started driving along the road'.format(self.model))

    def act(self):
        if self.fuel <= 50:
            self.tank_up()
            print('{} is refueled'.format(self.model))
        elif isinstance(self.place, Road):
            self.ride()



class AutoLoader(Vehicle):

    def __init__(self, model, bucket_capacity, warehouse=None, type='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = type
        self.truck = None

    def __str__(self):
        res = super().__str__()
        if self.truck == None:
            return res + ' waiting for truck...'
        else:
            return res + ' shipping {} goods'.format(self.truck)

    def act(self):
        if self.fuel <= 50:
            self.fuel += 500
            print('{} is refueled'.format(self.model))
        else:
            return

    def load(self):
        pass

    def unload(self):
        pass


TOTAL_CARGO_KG = 500000

Odessa = Warehouse(name='Odessa', content=TOTAL_CARGO_KG)
Kyiv = Warehouse(name='Kyiv', content=0)

odessa_kyiv = Road(start=Odessa, end=Kyiv, distance=490)
kyiv_odessa = Road(start=Kyiv, end=Odessa, distance=530)

Odessa.set_road_out(odessa_kyiv)
Kyiv.set_road_out(kyiv_odessa)

loader_1 = AutoLoader(model='Zaporozh CG-220', bucket_capacity=750, warehouse=Kyiv, type='unloader')
loader_2 = AutoLoader(model='Everun U-160', bucket_capacity=1000, warehouse=Odessa, type='loader')

truck_1 = Truck(model='Volvo KD-100', body_space=10000)
truck_2 = Truck(model='Mercedes JC-122', body_space=8000)

Odessa.truck_arrived(truck_1)
Odessa.truck_arrived(truck_2)

hour = 0

# while True:
for _ in range(5):
    hour += 1
    cprint('=============== {} hour ==============='.format(hour), color='yellow')
    truck_1.act()
    truck_2.act()
    loader_1.act()
    loader_2.act()
    cprint(truck_1, color='cyan')
    cprint(truck_2, color='cyan')
    cprint(loader_1, color='cyan')
    cprint(loader_2, color='cyan')
    cprint(Odessa, color='cyan')
    cprint(Kyiv, color='cyan')
