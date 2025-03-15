errno = 50159747054
name = 'Bob'

print(f'Hello, {name}!')

a, b = 5, 10
print(f'Five plus ten is {a+b} and not {2*(a+b)}')

def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

print(greet('Bob', 'going'))

print(f"Hey {name}, there's a {errno:#x} error!")
