class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

t = Test()
print('--Single Leading Underscore--')
print(t.foo)
print(t._bar)

print('-'*10)

from my_module import *
print(external_func())
# print(_internal_func())

print('-'*10)

import my_module
print(my_module.external_func())
print(my_module._internal_func())

print('--Single Trailing Underscore--')
# def make_object(name, class):
def make_object(name, class_):
    pass

