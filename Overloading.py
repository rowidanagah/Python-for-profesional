class A:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a + other

    def __radd__(self,other):
        return other + self.a

print(A(1) + 2 , 3+A(2))
print( "On strings be like l : {} , r: {} ".format(A('a') + 'b' , 'b' + A('a')))



class B:
    def __init__(self, b):
        self.b = b
    def __iadd__(self, other):
        # As well as a corresponding inplace version, starting with __i:
        self.b += other
        print("iadd")
        return self ## not that not allowed to return self.b in __iadd_ 

b = B(2)
print(b.b )# Out: 2
b += 1 # prints iadd
print(b.b )



"""
    __call__ , is a built-in methed that is used to write classes
       where the instances behave like functions and can be called like a function.
"""

class produt(object):
    def __init__(self, first):
        self.first = first
    # a(...)
    def __call__(self, second):
        return self.first * second

add2 = produt(2)
print("__call__(1 * 2) : " , add2(1) )# 3
print("__call__(2 * 2) : " , add2(2))