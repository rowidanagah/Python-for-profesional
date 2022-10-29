class ContextManager(object):
	"""docstring for ContextManager"""
	def __init__(self):
		pass
		
	def __enter__(self):
		print("__enter__()")
		# optionaly return an obj
		return "an instance"

	def __exit__(self , exc_type , exc_val , traceback):
		print("__exit__ with " , exc_val if exc_val else ' nope')



class ManageFile(object):
	"""Our ManageFile class follow/adhere the context manager protocole
	and support the with statment just sane as the `open` do """
	def __init__(self, name):
		self.name = name
		
	def __enter__(self):
		print("Opening the file")
		self.file = open(self.name , 'w+')
		return self.file

	def __exit__(self , exc_type , exc_val , traceback):
		print("__exit__ with " , exc_val if exc_val else ' nope')
		if self.file:
			self.file.close()

# -------------------------------------------------------------- #
with ContextManager() as e:
	print("is a " , e)

# -------------------------------------------------------------- #

print()
with ManageFile('test_ch30.txt') as file :
	file.write('Blew the lid of ur life')
	file.write('Bye for now')




"""
 Multiple context managers
"""

with open('test_ch30.txt') as input_file, open('test_ch77.txt', 'w') as output_file:
	# do something with both files.
	# e.g. copy the contents of input_file into output_file
	for line in input_file:
		output_file.write(line + '\n')


# It has the same effect as nesting context managers:
with open('test_ch30.txt') as input_file:
	with open('test_ch77.txt', 'w') as output_file:
		for line in input_file:
			output_file.write(line + '\n')




"""
Manage Resources
"""


class File():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
	def __enter__(self):
		self.open_file = open(self.filename, self.mode)
		return self.open_file
	def __exit__(self, *args):
		self.open_file.close()


for _ in range(10000):
	with File('test_ch30.txt', 'w') as f:
		f.write('foo')







