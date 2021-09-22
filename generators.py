print(sum(i for i in range(10) if i%2)) ## This is called a generators as a regexpress 
print(any(i%2 for i in range(2,10)))
"""
instead of usingthis 
"""
print((sum(i for i in range(10) if i%2))) ## Avoid duplication of `()` by using generators
print((any(i%2 for i in range(2,10))))


def contorous(func):
	def decor(*args):
		return func(*args)
	return decor

@contorous
def fun(lst):
	return sum(lst)


print(fun([i for i in range(4)]))