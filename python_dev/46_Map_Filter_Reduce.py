# MAP
cube = lambda x: x*x*x
print(cube(2))
l = [1,2,3,4,6,7]
# newl = []
# for item in l:
#     newl.append(cube(item))
newl = list(map(cube, l))
print(newl)

# FIlTER

def filter_function(a):
    return a>=4
newnewl = list(filter(filter_function, l))
print(newnewl)

from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)