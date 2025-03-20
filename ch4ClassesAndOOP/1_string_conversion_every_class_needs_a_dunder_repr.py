class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

my_car = Car('red', 37281)

print(my_car)
print(my_car.color, my_car.mileage)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'
    
    def __repr__(self):
        return '__repr__ for Car'
       
my_car = Car('red', 37281)
print(my_car)
print(str(my_car))
print(repr(my_car))


import datetime
today = datetime.date.today()

print(str(today))
print(repr(today))


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # def __repr__(self):
    #     return f'Car({self.color!r}, {self.mileage!r})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})'
    
my_car = Car('red', 37281)
print(my_car)


### COMPLETE EXAMPLE
class Car:
    def __init__(self, color, mileage):
        self.color = color 
        self.mileage = mileage

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mileage!r})')

    def __str__(self):
        return f'a {self.color} car'
    
my_car = Car('red', 37281)
print(repr(my_car))
print(str(my_car))
