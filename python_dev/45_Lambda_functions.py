# def double(x):
#     return x*2
def apply(fx,value):
    return 6 + fx(value)

import math
double = lambda x: x*2
square = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y:math.floor((x + y) /2)

print(double(5))
print(square(5))
print(cube(5))
print(avg(24,50))
print(apply(cube, 2))