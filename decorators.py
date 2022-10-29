
"""
Decorator is as a software design pattern, as they alter the fuctionality of a function,
 method or class without editing thier source of coded.

 Decorator function extends the functionality of another function without explicitly modifying it.

"""

def super_secret_function(func):
	return func

@super_secret_function ## this is same super_secret_function = super_secret_function(Voala)
def Voala():
	print('Hola hola')

Voala()



def decorator(f):
	"""
	However, note that this fuction return nothing and hence remove 
	 the decorated functions from the local scope
	"""
	pass

@decorator ## this is same as  hola = decorator(hola)
def hola():
	print('Hola hola hola ,this function is no longer called')
#hola() can't call this function as it will eraise an error 

from operator import mul


## to multiply

def decorator_to_mul(func):
	def inner_mutiplication(*args):
		print(args)
		return func(*args)
	return inner_mutiplication

@decorator_to_mul
def mutiplication(a,b):
	print("dana")
	return mul(3,2) # a*b

print(mutiplication(3,4))


print('decorator with args')

def dec(msg):
	def inner_dec(func):
		def msg_dec(*args):
			print('Vola, {}'.format(msg))
			return func(*args)
		return msg_dec
	return inner_dec

@dec('Below the lid of ur life')
def hola():
	return mul(2,3)

print(hola())

def singleton(cls):
	instance = [None]
	def wrapper(*args, **kwargs):
		if not instance[0] :
			instance[0] = cls(*args, **kwargs)
		return instance[0]
	return wrapper

@singleton
class singletone_class(object):
	"""docstring for singletone_class"""
	x = 9
	def __init__(self):
		print("Not yet...!")
		
print(singletone_class().x)
arr = [9,2,3]
lst = map(lambda n: n ** 2 if n % 2 == 0 else None, arr)
print(lst)