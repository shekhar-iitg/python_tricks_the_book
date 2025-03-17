def greet():
    """Return a friendly greeting."""
    return 'Hello!'

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

decorated_greet = uppercase(greet)

print(greet.__name__,'\n',greet.__doc__)
print(decorated_greet.__name__,'\n',decorated_greet.__doc__)


import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'

print(greet.__name__)
print(greet.__doc__)
