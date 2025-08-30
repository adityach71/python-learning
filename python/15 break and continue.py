for i in range( 12):
    print("5 X", i, "=", 5 * (i+1))
    if(i == 10):
       break #it will say that leave the rest and exit the code
for i in range(1, 6):
    if i == 3:
        continue   # skips printing 3, goes to next
    print(i)

while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break