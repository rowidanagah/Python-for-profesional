from  threading import Thread, current_thread
import os
from time import time, sleep
from multiprocessing import Process

def process():
	sleep(2)

start = time()

process()

print("dif" , time() - start)

start = time()

thrds = [Thread(target = process) for _ in range(3)]

for t in thrds:
	t.start()

for t in thrds:
	t.join()


"""
Note that even each process takes 2 sec to run, the total diffrance in time
 will be the time that one process takes that's why the whole processes 
 together were able to run together in parallel.

"""

print("dif" , time() - start)




# ------------------------------------------------------------------------- #


def func(i):
	return i ** 2

def otherfunc(m, i):
	return m * i

def process():
	for i in range(100):
		res = 0
		for j in range(10000):
			res = otherfunc(res , func(i))

start = time()



# ------------------------------------------------------------------------- #

"""
To run a function in another thread
 
"""
def process():
	print("PID Is {} , Thread is {} ".format(os.getpid(), current_thread().name))


thrds = [Thread(target = process) for _ in range(3)]

for t in thrds:
	t.start()

for t in thrds:
	t.join()

