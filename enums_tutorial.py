from enum import Enum

class Color(Enum):
	red,w,h = 0,1,2

print(Color(0))
print(Color.red)
print(Color['red'])

class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3

# we can loop over a enum obj
for shake in Shake:
    print(shake)

"""
Enumeration members are hashable, so they can be used in dictionaries and sets:

"""
apples = {}
apples[Color.red] = 'red delicious'
apples[Color.w] = 'granny smith'
apples == {Color.red: 'red delicious', Color.w: 'granny smith'}
print("Hashable improvment" , [(apples[i], i )for i in apples])



##print(color[0])

a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}
a.union(b)
#print(a ,b , a.union(b))


def foo():
    if True:
        a = 5
    print(a) # ok

print(foo())


a = 'global'
class Fred:
    a = 'class'  # class scope
    b = (a for i in range(10))  # function scope
    c = [a for i in range(10)]  # function scope
    d = a  # class scope
    e = lambda: a  # function scope
    f = lambda a=a: a  # default argument uses class scope
   
    @staticmethod  # or @classmethod, or regular instance method
    def g():  # function scope
        return a

print(Fred.f())
print(Fred.e())
print(next(Fred.b))


print('a'  , a)
class A:
    a = 42
    b = [i for i in range(10)]

print(A.b)



"""
the else clause only executes after a for loop terminates by iterating to completion, or after a while loop
terminates by its conditional expression becoming false
"""
for i in range(3):
    print(i)
else:
    print('done')

import json

"""
json.dumps() function converts a Python object into a json string.
"""

data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"} , 
{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"} 

]}

#print(json.dumps(data , indent = 2 ) )


datat_str = {"foo": "bar", "baz": []} ## same as  {u"foo": u"bar", u"baz": []}
print(json.dumps(datat_str , indent = 2 ) )

from itertools import islice

print([i for i in islice(range(20),2 , 10)])

##islice(iterable, start, stop, step)
li = [2, 4, 5, 7, 8, 10, 20] 
  
# Slicing the list
print(list(islice(li, 1, 6, 2)))


print("Test rowida branch")