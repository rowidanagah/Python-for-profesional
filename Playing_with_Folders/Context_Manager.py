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
