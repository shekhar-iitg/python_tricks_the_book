from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
print(Car)

Car = namedtuple('Car', [
    'color',
    'mileage',
])
print(Car)

my_car = Car('red', 3812.4)
print(my_car.color, my_car.mileage)
print(my_car[0], tuple(my_car))

color, mileage = my_car
print(color, mileage)
print(*my_car)

print(my_car)

my_car.color = 'blue'
