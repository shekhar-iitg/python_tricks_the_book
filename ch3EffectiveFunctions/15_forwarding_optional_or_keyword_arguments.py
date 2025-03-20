def bar(x, *args, **kwargs):
    print(x, args, kwargs)

def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)

foo('hello', 1, 2, 3, key1='value', key2=999)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

print(AlwaysBlueCar('green', 48392).color)

import functools

def trace(f):
    @functools.wraps(f)
    def decorated_functions(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_functions

@trace
def greet(greeting, name):
    return f'{greeting}, {name}'

greet('Hello', 'Bob')
