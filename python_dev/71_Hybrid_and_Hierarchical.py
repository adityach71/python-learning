# Hybrid Inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Hierarchical Inheritance
class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass