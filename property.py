"""
	The @property decorator can be used to define methods in a class which act like attributes.

	@property is used to get the value of a private attribute without using any getter methods.
	 We have to put a line @property in front of the method where we return the private variable.

"""


class Cash:
	def __init__(self, val):
		self.val = val

	@property
	def format(self):
		return "{:.2f}".format(self.val)

	@format.setter
	def format(self , new):
		self.val = float(new[1:])


cash = Cash(3.59)

print(cash.format)

cash.format = '$123.45'
print(cash.format)



class BaseClass(object):
	@property
	def foo(self):
		return some_calculated_value()
	@foo.setter
	def foo(self, value):
		do_something_with_value(value)

class DerivedClass(BaseClass):
	@BaseClass.foo.setter
	def foo(self, value):
		do_something_different_with_value(value)