from collections import namedtuple

Car = namedtuple('Car', [
    'color',
    'mileage',
])

my_car = Car('red', 3812.4)

print(my_car._asdict())
print(my_car._replace(color='blue'))
print(my_car)

my_purple_car = Car._make(['purple', 999])
print(my_purple_car._asdict())
