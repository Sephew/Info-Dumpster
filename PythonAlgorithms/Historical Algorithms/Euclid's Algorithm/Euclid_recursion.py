import math

def func(x,y):
    smaller = min(x,y)
    larger = max(x,y)
    remainder = larger % smaller
    if (remainder == 0):
        return smaller
    elif (remainder != 0):
        return func(smaller,remainder)

print(func(10,3))