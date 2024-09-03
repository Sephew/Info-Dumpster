import math
# Although Euclid made alot of algorithms, his most famouse one is the algorithm to find the greatest common denominator
# A = q1 * B + C
# B = q2 * C + D
# C = q3 * D + E
# so on and so fort until the trailing constant becomes 0.
def func(x,y):
    smaller = min(x,y)
    larger = max(x,y)
    remainder = larger % smaller
    if (remainder == 0):
        return smaller
    elif (remainder != 0):
        return func(smaller,remainder)

print(func(10,3))
