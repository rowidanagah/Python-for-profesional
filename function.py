def f(*args):
	'''
	Note that args is just a name. 
	You’re not required to use the name args.
	 You can choose any name that you prefer,
	'''
	return a+b+c

def concatenate(**kwargs):
	"""
	**kwargs works just like *args,
	but instead of accepting positional arguments it accepts keyword (or named) arguments
	"""
	for i,v in kwargs.items():
		return i,v
a, b, c = 1,2,3
l2 =[1,2,3]
l1 = [a, b, c]

X = ['Rowida' , 'Dana' , 'Anas']
x = dict(zip( X , [i+1 for i in range(3)]))
print(f(l1))
print(f(a,b,c))
print(x)


concatenate(**x)


# correct_function_definition.py
def my_function(a, b, *args, **kwargs):
    pass

"""
# correct_function_definition.py
def my_function_uncorrect(a, b,**kwargs, *args):
    pass
"""


def closure_inc(x):
	"""
	closure in python is when function is created
	"""
	def inc(y):
		"""
		1- note each call will fully inhert the vals of its enclosing environment.
		2- to paly with the val or content of x, we first need to call x as a nonlocal val
		nonlocal x 
		y += x 
		"""
		return x + y
	return inc

clouser = closure_inc(2)
print(clouser(2))



"""
functional programing to make a problem into a set of functions, with 
functions that don't have any state that will affect the output
"""


"""
Partial Functions in ch 56
"""
def f(a,b,c):
	return a*100 + b*10 + c

print('f(1,1,1)' ,f(9,1,1))
from functools import partial
g = partial(f,1,1)
print(g(5))


## @lru_cashe()
def fib(n):
	if n < 2 :
		return n 
	return fib(n-1) + fib(n-2)