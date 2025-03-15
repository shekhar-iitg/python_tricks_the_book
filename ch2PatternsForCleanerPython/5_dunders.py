class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42

t = Test()
# print(dir(t))

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'Overridden'
        self._bar = 'Overridden'
        self.__baz = 'Overridden'

e_t = ExtendedTest()
print(dir(e_t))

print(f'__baz of ExtendedTest Instance: {e_t._ExtendedTest__baz}')
print(f'__baz of Test Instance: {t._Test__baz}')
print(e_t.__baz)