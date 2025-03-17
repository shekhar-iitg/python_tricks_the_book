def yell(text):
    return text.upper() + '!'

bark = yell

funcs = [bark, str.lower, str.capitalize]

for f in funcs:
    print(f, f('hey there'))

print(funcs[0]('heyho'))
