class exp(Exception):
	pass


x = 1 
try :
	print(exp('Hola'))
except Exception as e:
	print("Try to catch" , e)
	pass
else:
	pass
finally:
	pass


"""
		CH 90
"""
def dif():	
	"""
	Note we can't call the d_inner outside of this function scope 
	while d is accessable 
	The reason is the for loop in inside another scope :::> Scope of the function def
	"""
	for _ in range(7):
		d_iner = _ * 2

for _ in range(7):
	d = _ * 2

print(d)

def f(a):
	return a*2

a,b,c = 1,2,3
#print(f(a,b,c))

a,b = {1,2}, {3,4}
print(a+b)

