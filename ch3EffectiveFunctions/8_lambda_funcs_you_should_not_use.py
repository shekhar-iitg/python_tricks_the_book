# Harmful:
class Car:
    rev = lambda self: print('Wroom!')
    crash = lambda self: print('Boom!')
    
    # def crash_better(self):
    #     print('Boom!')

my_car = Car()
my_car.crash()
# my_car.crash_better()


# Harmful:
print(list(filter(lambda x: x % 2 == 0, range(16))))
# Better:
print([x for x in range(16) if x % 2 ==0])
