class Trac:
	"""docstring for Trac"""
	def __init__(self, ):
		print("Initialzed")

	def __del__(self):
		print("ALeardy broken")


def foo():
	Trac()
	print("------------------")
	t = Trac()
	print("------------")
	del t 


foo()
