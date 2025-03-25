class Base:
    def foo(self):
        raise NotImplementedError()
    
    def bar(self):
        raise NotImplementedError()
    

class Concrete(Base):
    def foo(self):
        return 'foo() called'
    
    # On no, we forgot to override bar()...
    # def bar(self):
    #     return 'bar() called'

b = Base()
try:
    print(b.foo())
except NotImplementedError:
    print('NotImplementedError in Base')
finally:
    try:
        c = Concrete()
        print(c.foo())
        print(c.bar())
    except NotImplementedError:
        print('NotImplementedError in Concrete')



from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

    # We forget to declare bar() again...

assert issubclass(Concrete, Base)

c = Concrete()
