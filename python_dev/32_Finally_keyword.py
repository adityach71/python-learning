def fun1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Error is coming")
        return 1
    finally:
        print("I am always executed")
        print("I am always executed")


x = fun1()
print(x)