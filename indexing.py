class MultiIndexing:
	def __init__(self , val):
		self.val = val

	def __repr__(self):
		return repr(self.val)

	def __getitem__(self , item):
		"""
		To get a spesific item if it's ans ins :GET it form the self.val
		else get idex of self.val value
		"""

		if isinstance(item , (int , slice)):
			return self.__class__(self.val[item]) 
		else :
			## raise ValueError('Cannot find the item in the slice')
			return [self.val[i] for i in item] 

	def __setitem__(self , item , val):
		"""
		To edits items 
		- To specify a single element index :: It's OK `[2]`
		- To edit a slice :: Not acceptable  `[:3]` 
		- More that one index of ints :: OK Acceptable `[1,2,3]` >Loop throught them
		- More than one index in a slice foramt is not acceptable `indx[1,3,2:] = -1`
		"""
		if isinstance(item , int):
			self.val[item] = val
		elif isinstance(item , slice):
			raise ValueError('TypeError: can only assign an iterable')
		else :
			for it in item:
				if isinstance(item , slice):
					raise ValueError('TypeError: can only assign an iterable')
				self.val[it] = val

	def __delitem__(self , item):
		"""
		We can del item weither it's an int, a slice `:3`
		or list of indexes that cann't contain any slice within not [1,3,:3]
		as we will sort this lst of indexws as del each elelment of them
		"""
		if isinstance(item , int) or isinstance(item , slice):
			del self.val[item]
		else :
			if any(isinstance(i , slice) for i in item):
				raise ValueError('can only assign an iterable')
			item = sorted(item , reverse = True)
			for i in item:
				del self.val[i]




indx = MultiIndexing([i for i in range(1,9)])
print(indx)
print(indx[1,5,2,6,1])
print(indx[1,5:,4]) ## Notice the slicing here
indx[3,6,4] = 6
print(indx) ## Single item to be edited :: OK
indx[0] = 10
print(indx)

s = [i for i in range(1,5)]
del indx[1,4,3] 
print(indx)

"""
--------------------------------------------- Ch67 Generators -----------------------------------------------
"""

def f():
	for i in range(10):
		yield i**2

print(f())
f = f()
print(next(f))
print(next(f))
print(next(f))



