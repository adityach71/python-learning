# This is the 1st one
a = int(input("Enter your age:"))
print("Your age is:", a)
# Conditional operators
# >,<,>=,<=,==
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
b = "You are eligible for driving!"
c = "You cannot drive!!"
if(a>=18):
    print(b.title())
    print("Yes")
else:
    print(c.title())
    print("No")
print("Yay!")
# This is the 2nd one
applePrice = 10
budget = 200

if(budget - applePrice >= 50):
    print("You can buy 1kg apple")

elif (budget - applePrice >= 70):   
    print("Its Okay you can buy")
else:
    print("You cannot buy apple")
# This is the 3rd one
num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negetive")
elif (num == 0):
    print("Number is 0")
else:
    print("Number is positive")

print("I am happy now")
# This is the 4th one
num = 18
if (num < 0):
    print("Number  is negative.")
elif (num > 0):
    if(num > 10):
        print("number is between 1-10")
    elif(num <= 10):
        print("Number is greater ten 20")
    else:
        print("Number is greater then 20")
else:
    print("number is zero")