a = int(input("Enter any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")


a = int(input("Enter any value between 5 and 9 (or type Quit)"))  # this is a quick quiz
if a=="Quit":
    print("No problem come back later")
else:
    a = int(a)
    if a < 5 or a > 9:
        raise ValueError("Value should be between 5 and 9")
    else:
        print("You entered:", a)