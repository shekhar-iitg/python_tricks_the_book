def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper

@trace 
def say(name, line):
    return f'{name}: {line}'

print(say('Jane', 'Hello, World'))
