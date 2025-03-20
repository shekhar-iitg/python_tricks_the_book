def foo1(value):
    if value:
        return value
    else:
        return None
    
def foo2(value):
    """Bare return statement implies  `return None`"""
    if value:
        return value
    return

def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value
    
print(type(foo1(0)), type(foo2(0)), type(foo3(0)))
