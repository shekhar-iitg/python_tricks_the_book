def yell(text):
    return text.upper() + '!'

print(yell('hello'))

bark = yell

print(bark('woof'))

del yell

try:
    yell('hello?')
finally:
    print(bark('hey'))
    print(bark.__name__)
