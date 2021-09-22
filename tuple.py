## ch 28
tup = 2,3,4,5 ## note it's not nececcary to write the '()'
print(type(tup))

t1 , ta = (1) , ('a') ## note that a single value inside the '()' it's not a tuple
print(type(t1) , type(ta))

"""
that's why u've to add comma rigth after the single val
this called a singletone, which is not recommended by PEP8
"""
t1 , ta = (1,) , ('a',) ## note that a single value inside the '()' it's not a tuple
print(type(t1) , type(ta))

"""
 tuple is immutable
  and does not have .append() or .extend method 
   however useing += is possible as it's a way to create anothor new tuple with the new val added
    the old tuple is not changed but it's replaced.
"""

t = (1,2)

print(id(t))

t += (2,3)
print(id(t)) ## note the diff of the id after and before the += operation, that's whya new tuple have been created
file = open('Password.log')
file.seek(2)
opt = file.tell()
print(opt)

