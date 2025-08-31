def calculation(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isGreater(a, b):
    if a > b:
        print("first is greater")
    else:
        print("second is greater or equal")


def islesser(a, b):
    pass


a = 9
b = 8
isGreater(a, b)
# gmean1 = (a * b)/(a + b)
# print(gmean1)
calculation(a, b)
c = 8
d = 7
gmean2 = (c * d) / (c + d)
print(gmean2)
calculation(c, d)
isGreater(c, d)
