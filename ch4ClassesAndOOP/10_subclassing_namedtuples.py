from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'
        
c = MyCarWithMethods('red', 6337)
print(c.hexcolor())


Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple(
    'ElectricCar', Car._fields + ('charge',)
)
ec = ElectricCar('red', 1234, 45.0)

print(ec)
