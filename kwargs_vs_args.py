def func(foo , ky):
	"""
	**kwargs keys must be the same vals as the func parameters
	"""

	return foo, ky

X = ['Rowida' , 'Dana' , 'Anas']
x = dict(zip(X, [i+1 for i in range(3)]))


def func_kwargs(**kwargs):
	# return kwargs if kwargs else 0
	return kwargs if kwargs else kwargs.get('val',0)

dic = dict(zip(['foo' , 'ky'],[i+1 for i in range(2)]
	))

print(x)
print("We can pass a non val as a **kwargs , See : ",func_kwargs())
print(func_kwargs(**x))
print(func(**dic))




def print_args(arg1, arg2):
	print(str(arg1) +str(arg2))

l1 = (1,2)
l2 = (3,4)
print_args(l2,l1)
print_args(*l1) ## Concatenation 




"""
* with the zip is usedto reverse the functionality of zip

Follow to see 
"""

zipped = zip(l1,l2)
print(zipped) 
print([(i,j) for i,j  in zipped])
rev = zip(*zipped)
print([i for i in rev])