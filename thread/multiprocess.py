from time import time, sleep
from multiprocessing import Process

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

process()

print("dif of one run took " , time() - start)

start = time()

prs = [Process(target = process) for _ in range(3)]

for t in prs:
	t.start()

for t in prs:
	t.join()

print("dif of 2 runs took " , time() - start)
