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
		Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access 
		"""
		return "Oh shit here we go again"




my = MyClass()
print(my.method())
print(my.classmethod())
print(my.staticmethod())
print(type(1))
