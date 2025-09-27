a = [1,2,43]
b = [1,2,43]

print(a is b) # use to compair exact location of an object in memory
print(a == b) # use to compair value

a = 3
b = 3

print(a is b)
print(a == b)

a = "Aditya"
b = "Aditya"

print(a is b)
print(a == b)

a = (1,2)
b = (1,2)

print(a is b)
print(a == b)

a = None
b = None

print(a is b)
print(a == None)