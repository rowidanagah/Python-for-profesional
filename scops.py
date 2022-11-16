a = 'global'
class Fred:
 a = 'class' # class scope
 b = (a for i in range(10)) # function scope
 c = [a for i in range(10)] # function scope
 d = a # class scope
 e = lambda: a # function scope
 f = lambda a=a: a # default argument uses class scope
 
 @staticmethod # or @classmethod, or regular instance method
 def g(): # function scope
   return a
print(Fred.a) # class
print(next(Fred.b)) # global
print(Fred.c[0]) # class in Python 2, global in Python 3
print(" d  " , Fred.d) # class
print(Fred.e()) # global
print(Fred.f()) # class
print(Fred.g()) # global