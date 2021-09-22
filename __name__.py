"""
__name__ :: used to check whether a file has been imported as a module or not 

tp check whether the module is being run by itself
"""



def decorator_to_mul(func):
	def inner_mutiplication(*args):

		print('__name__ of func is : Entering ' , func.__name__)
		res =  func(*args)
		print('__name__ of func is: exiting' , func.__name__)

		return res
	return inner_mutiplication

@decorator_to_mul
def mutiplication(a,b):
	return a * b

print(mutiplication(3,4))