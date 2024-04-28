'''

'''


def decorator(addition):
    def inner(x,y):
        a=addition(x,y)
        add=a+10
        return add
    return inner

@decorator
def addition(x,y):
    return x+y
print(addition(1,2))

