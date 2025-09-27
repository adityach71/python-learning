x = 4
print(x)

def hello():
    x = 5
    print(f"The local x is {x}")
    print("Hello Aditya")


print(f"The globle x is {x}")
hello()
print(f"The globle x is {x}")



x = 10

def my_function():
    global x
    x = 4
    global y
    y = 5
    print(y)

my_function()
print(x)
print(y)