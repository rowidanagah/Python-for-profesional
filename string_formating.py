class MyClass:
	def method(self):
		return "Oh shit here we go again", self

	@classmethod
	def classmethod(cls):
		"""
		Because the class method only has access to this cls argument, it can’t modify object instance state. 
		That would require access to self. However, 
		class methods can still modify class state that applies across all instances of the class.
		"""
		return "Oh shit here we go again", cls

	@staticmethod
	def staticmethod():
		"""
		This type of method takes neither a self nor a cls parameter.
		Therefore a static method can neither modify object state nor class state.
		Static methods are restricted in what data they can access 
		"""
		return "Oh shit here we go again"


my = MyClass()
print(my.method())
print(my.classmethod())
print(my.staticmethod())
print(type(MyClass))
print('+=====================================================String Formating+==================================================')

X = ['Rowida' , 'Dana' , 'Anas']
print("Simple form of formating")
print('Loop over names in this list {},{} and {}'.format(X[0] , X[1] , X[-1]))
print('Loop over names in this list {},{} and {}'.format(*X))
print(map('Loop over names in this list {},{} and {}'.format , X)) ## map doesn't work for python 3



print('+=====================================================String Formating+==================================================')

print('To specify the ordering of strs ::: write the index inside the 	`{}`')
print('Loop over names in this list {0},{2} and {1}'.format(X[0] , X[1] , X[-1]))
print('More the the provided strs ::: write the index inside the 	`{}`')
print('Loop over names in this list {0},{2},{0} and {1} '.format(X[0] , X[1] , X[-1]))

print('+=====================================================Float Formating+==================================================')
print('With no Float after the point {0:.0f}'.format(123.12345))
print('With only one  Float after the point {0:.1f}'.format(123.12345))
print('With 2 Floats after the point {0:.2f}'.format(123.12345))

print('+====================================================Same hold for other way of referring+==================================================')
print('With no Float after the point {:.0f}'.format(123.12345))
print('With only one  Float after the point {:.1f}'.format(123.12345))
print('With 2 Floats after the point {:.2f}'.format(123.12345))

print('With 2 Floats , To specify with number to print wither by its name {amount:.2f}'.format(amount= 123.12345 , total = 321.90343))
print('With 2 Floats , To specify with number to print or by its index  {0:.2f}'.format(123.12345 , 321.90343))


print("To swap from Capital to small and vis versa" , "Oh shit here we go again".swapcase())

"""
If you need to replace each item we get a spasific set of char in str, instead of using replace to replace each encounter of a every chr,
 USE 'translate and maketrans ' ::
 'str.maketrans('','') to make the transilation of each item with another
 'str.translate(table , )'
"""
replace = str.maketrans('aio' ,'123') 
mystr = "Oh shit here we go again"
print(mystr.translate(replace))
## print('Oh shit here we go again'.translate(None , 'op'))
mystr = ' '
print([1 if mystr else 0])