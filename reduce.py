def mul(a,b):
	return '{} multiplay {} is {}\n '.format(a , b , a*b)

from functools import reduce
reduce_res = reduce(mul , [1,2,3] , 10)
print(type(reduce_res))
##print(reduce_res)
print(map(lambda x :x**x , [1,2,3]))

def arvg(*lst):
	return round(sum(lst) / len(lst) , 3)

def arg(lst):
	return round(sum(lst) / len(lst) , 3)

print(list(map(arvg , [1,2,3]))) ## note for this it's requirred more than one list
 
print(list(map(arvg ,list(range(10)), [3,4,5] ,[1,2,3])))
print(arg(list(range(10))))


class ListList:
	def __init__(self , val):
		self.val = val
		self.setofvalues = set(item for sublist in self.val for item in sublist)
	def __iter__(self):
		print("Useing __iter__")
		"""
		Note that the below line `the return ` we use only () to return the generator to allow instance to loop over if
		Don't use list , set or any iter only use generaotrs
		"""
		return (item for sublist in self.val for item in sublist)
	def __contains__(self , item):
		print('\n Useing __contains__')
		return item in self.setofvalues
lsts = ListList([[1,2,3,4] , [4,5,6,7]])
print(lsts.__iter__())
for i in lsts:
	print(i , end=' ')
print(4 in lsts)  ## Using contains
