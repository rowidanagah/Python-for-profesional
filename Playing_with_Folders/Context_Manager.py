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


with ContextManager() as e:
	print("is a " , e)
		