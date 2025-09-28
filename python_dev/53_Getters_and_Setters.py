class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        # return 10 times the actual _value
        return 10 * self._value

    @value.setter
    def value(self, new_value):
        # store the new value divided by 10
        self._value = new_value / 10


# Test
obj = MyClass(10)

print(obj._value)   # 10 (actual stored value)
print(obj.value)    # 100 (10 times _value)

obj.value = 50      # sets _value = 50/10 = 5
obj.show()          # Value is 5
print(obj.value)    # 50
