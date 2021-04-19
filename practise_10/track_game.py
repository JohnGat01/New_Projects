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
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return 'In {} warehouse {} KG goods.'.format(self.name, self.content)

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        truck.place = self
        print('{} arrived to warehouse {}.'.format(truck, self.name))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print('{} is ready warehouse - {}.'.format(truck, self.name))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return '{} has {} fuel'.format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000
        Vehicle.total_fuel += self.fuel
        print('{} is refueled'.format(self.model))


class Truck(Vehicle):
    dead_time = 0

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
            self.fuel -= 50
        else:
            self.fuel -= self.dictance_to_target * 0.625  # gasoline uses for the remaining distance to target
            self.dictance_to_target -= self.dictance_to_target
            self.place = self.place.end
            self.place.truck_arrived(self)
            print('{} is arrived'.format(self.model))
        self.fuel -= 50
        print('{} is going on the road, {} km left'.format(self.model, self.dictance_to_target))

    def go_to(self, road):
        self.place = road
        self.dictance_to_target = road.distance
        print('{} started driving along the road'.format(self.model))

    def act(self):
        if self.fuel <= 100:
            self.tank_up()
        elif isinstance(self.place, Road):
            self.ride()
        else:
            Truck.dead_time += 1


class AutoLoader(Vehicle):
    dead_time = 0

    def __init__(self, model, bucket_capacity, warehouse=None, type_of_al='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.type_of_al = type_of_al
        self.truck = None

    def __str__(self):
        res = super().__str__()
        if self.truck is None:
            return res + ' waiting for truck...'
        else:
            return res + ' shipping {} goods'.format(self.truck)

    def load(self):
        if self.warehouse.content <= 0:
            print('Nothing in warehouse {}'.format(self.warehouse))
            if self.truck:
                self.warehouse.truck_ready(self.truck)
                self.truck = None
                return
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest
        print('{} is loading {}...'.format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        if self.truck.cargo >= self.bucket_capacity:
            self.warehouse.content += self.bucket_capacity
            self.truck.cargo -= self.bucket_capacity
        else:
            self.warehouse.content += self.truck.cargo
            self.truck.cargo -= self.truck.cargo
        print('{} is unloading {}...'.format(self.model, self.truck))
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def act(self):
        if self.fuel <= 50:
            self.fuel += 500
            self.total_fuel += self.fuel
            print('{} is refueled'.format(self.model))
        elif self.truck is None:
            self.truck = self.warehouse.get_next_truck()
            if self.truck is None:
                AutoLoader.dead_time += 1
        elif self.type_of_al == 'loader':
            self.load()
        else:
            self.unload()


LOADERS_ALL = int(input('How much loaders do you have? '))
UNLOADERS_ALL = int(input('How much unloaders do you have? '))
TRUCKS_ALL = int(input('How much trucks do you have? '))
TOTAL_CARGO_KG = 500000

Odessa = Warehouse(name='Odessa', content=TOTAL_CARGO_KG)
Kyiv = Warehouse(name='Kyiv', content=0)

odessa_kyiv = Road(start=Odessa, end=Kyiv, distance=490)
kyiv_odessa = Road(start=Kyiv, end=Odessa, distance=530)

Odessa.set_road_out(odessa_kyiv)
Kyiv.set_road_out(kyiv_odessa)

loaders = []
for number in range(LOADERS_ALL):
    loader = AutoLoader(model='Jeep G-2 #{}'.format(number), bucket_capacity=2000, warehouse=Odessa, type_of_al='loader')
    loaders.append(loader)

unloaders = []
for number in range(UNLOADERS_ALL):
    unloader = AutoLoader(model='Zaporozh CG-220{}'.format(number), bucket_capacity=1000, warehouse=Kyiv,
                          type_of_al='unloader')
    unloaders.append(unloader)

trucks = []
for number in range(TRUCKS_ALL):
    truck = Truck(model='Volvo KD-100 #{}'.format(number), body_space=10000)
    Odessa.truck_arrived(truck)
    trucks.append(truck)

hour = 0

while Kyiv.content < TOTAL_CARGO_KG:
    hour += 1
    cprint('=============== {} hour ==============='.format(hour), color='yellow')
    for truck in trucks:
        truck.act()
    for loader in loaders:
        loader.act()
    for unloader in unloaders:
        unloader.act()
    Odessa.act()
    Kyiv.act()
    for truck in trucks:
        cprint(truck, color='cyan')
    for loader in loaders:
        cprint(loader, color='cyan')
    for unloader in unloaders:
        cprint(unloader, color='cyan')
    cprint(Odessa, color='cyan')
    cprint(Kyiv, color='cyan')

print(Vehicle.total_fuel, 'litres gas')
print(Truck.dead_time, 'trucks dead time')
print(AutoLoader.dead_time, 'auto-loaders dead time')
cprint('{} hours takes transportation'.format(hour), on_color='on_green')
