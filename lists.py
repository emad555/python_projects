def foo(*x):
    z = [i.upper() for i in x]
    return sorted(z) 


print(foo("hi","by"))