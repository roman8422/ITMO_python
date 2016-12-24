# Разными классами создаем поезд с разными вагонами: грузовые, пассажирские, плацкартные.
# У каждого вагона своя стоимость места, количество мест.
# Нужно посчитать заработок всего поезда

class Train:

    def __init__(self, distance):
        self.distance = distance
        self.cars = []

    def get_total_price(self):
        price = 0
        for car in self.cars:
            price += car.get_ext_price()
        return price

class Car:
    def __init__(self, train):
        train.cars.append(self)
        self.distance = train.distance

    def get_ext_price(self):
        return self.distance * self.price * self.price_units # количество мест

class RailCar(Car): # грузовой вагон
    price_units = 100
    price = 1500

    def __init__(self, train):
        super().__init__(train)
        self.price_units = RailCar.price_units
        self.price = RailCar.price

class PassengerCar(Car): # плацкартный вагон
    price_units = 120
    price = 1000

    def __init__(self, train):
        super().__init__(train)
        self.price_units = PassengerCar.price_units
        self.price = PassengerCar.price

class CompartmentCar(Car): # купейный вагон
    price_units = 30
    price = 3000

    def __init__(self, train):
        super().__init__(train)
        self.price_units = CompartmentCar.price_units
        self.price = CompartmentCar.price


t = Train(500)
vagon1 = PassengerCar(t)
vagon2 = CompartmentCar(t)
vagon3 = RailCar(t)

print(t.cars)
print(t.get_total_price())
for car in t.cars:
    print(car.get_ext_price())
