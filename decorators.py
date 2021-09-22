
"""
Decorator is as a software design pattern, as they alter the fuctionality of a function,
 method or class without editing thier source of coded

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


## to multiply

def decorator_to_mul(func):
	def inner_mutiplication(*args):
		print(args)
		return func(*args)
	return inner_mutiplication

@decorator_to_mul
def mutiplication(a,b):
	return a * b

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
	pass

hola()

