class Dog:
    num_legs = 4    # <- Class variable

    def __init__(self, name):
        self.name = name    # <- Instance Variable

jack = Dog('Jack')
jill = Dog('Jill')
print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)

print(Dog.num_legs)
try:
    print(Dog.name)
except AttributeError:
    print('AttributeError')
finally:
    Dog.num_legs = 6
    print(jack.num_legs, jill.num_legs)

    Dog.num_legs = 4
    jack.num_legs = 6
    print(jack.num_legs, jill.num_legs, Dog.num_legs)

    print(jack.num_legs, jack.__class__.num_legs)
