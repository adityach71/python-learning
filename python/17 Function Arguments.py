def avarage(a=9, b=1):
    print("The avarage is ", (a + b) / 2)


# avarage()
avarage(1, 5)
avarage(
    b=9, a=21
)  # if you want to arange the numbers without the function order you can use this way to decleare the object value

# for i in range(1000):
#     print("Love ❤️  you")


def name(fname, mname="Aditya", lname="Choudhary"):
    print("Hello! ", fname, "and", mname, lname)


name("Amy")

def avarage(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is: ", sum / len(numbers))
# avarage(5,6,7,1)
    return sum /  len(numbers)

c= avarage(5,6,7,1)
print(c)

def name(**name):
    print("Hello, ", name["fname"],
       name["mname"], name["lname"] )
    
name(mname = "Buchanan", lname = "Barnes", fname = "james")