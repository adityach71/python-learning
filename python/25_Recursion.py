# factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))

# fibonacci sequence
def Fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)
    
print(Fibonacci(6))