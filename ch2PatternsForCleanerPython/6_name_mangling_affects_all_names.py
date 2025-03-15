class ManglingTest:
    def __init__(self):
        self.__mangled = 'Hello'

    def get_mangled(self):
        return self.__mangled


class MangledMethod:
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()


_MangledGlobal__mangled = 23
class MangledGlobal:
    def test(self):
        return __mangled


print(ManglingTest().get_mangled())
print(MangledMethod().call_it())
print(MangledGlobal().test())

try:
    print(ManglingTest().__mangled)
finally:
    print(MangledMethod().__method())
