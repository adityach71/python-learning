a = True
print(a := False)

numbers = [1,2,3,4,5]

while (n := len(numbers)) > 0:
    print(numbers.pop())


foods = [] 

# working normally

while True:
    item = input("What food do you like?: ")
    if item.lower() == "quit":
        break
    foods.append(item)

print("Your favorite foods are:", foods)



# using walrus

foods = []

while (item := input("What food do you like?: ")) != "quit":
    foods.append(item)

print("Your favorite foods are:", foods)
