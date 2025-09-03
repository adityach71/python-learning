marks = [3,5,6, "Aditya", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[5]) # It will through a error. Thats mean the value is not defined thats simply means that i have not entered a value i the case of 5

# this all will print 6 because in the place value of 2 is 6
print(marks[-3]) #It is a Negetive index
print(marks[len(marks)-3]) # I have converted this into positive index
print(marks[5-3])
print(marks[2])


if "6" in marks:
    print("Yes")
else:
    print("No")

if "di" in "Aditya":
    print("Yes") #if i will enter "dta" insted of di it will print No thats means it dosent target the letter its target the sequance
else:
    print("No") 

print(marks)
print(marks[1:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)