## CH 117

from threading import Thread

def foo():
	print ("Hola Hola")

f1 = Thread(target = foo)

"""
	Thread will not be excuted unless `start` is called on the thread object

	Start will run and terminated.

	Calling `thread_name.start` again will cuase a `RuntimeError`
"""
print(f1.start())




"""
	Custom Thread : We must override the Thread class run function
"""

from time import sleep

class Sleepy(Thread):
	"""docstring for Sleepy"""
	def run(self):
		sleep(1)
		print("Voala !")

slp = Sleepy()
slp.start()
slp.join()
print("Custom Thread ~!")



