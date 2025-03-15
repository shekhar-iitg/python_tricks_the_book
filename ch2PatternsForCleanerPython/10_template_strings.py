from string import Template

errno = 50159747054
name = 'Bob'

t = Template('Hey, $name!')
print(t.substitute(name=name))


templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name=name, error=errno))


SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass

err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
print(user_input.format(error=err))

user_input = '${error.__init__.__globals__[SECRET]}'
print(Template(user_input).substitute(error=err))
