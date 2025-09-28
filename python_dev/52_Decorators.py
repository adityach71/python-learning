def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)  # call the original function
        print("Thanks for using this function")
    return mfx  # return the wrapper function

@greet
def hello():
    print("Hello")

@greet
def add(a, b):
    print(a + b)

# Using the decorated functions
hello()
add(5, 7)
