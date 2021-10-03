"""
Delay :: Is to add a delay  in prog excution time ,  It should be
 between two statements or between any part of the program code according to you. 

In order to add delay, import Slepp form time module

Syntax 
	`time.sleep(value)`

"""

from threading import Thread
from threading import Timer


from time import sleep

for i in range(4):
	print(i)
	# adding a 1 second time delay
	sleep(1)


from threading import Timer
import datetime

def f():
    print("Code to be executed after a delay at:", datetime.datetime.now().time())

print("Code to be executed immediately at:", datetime.datetime.now().time())
timer = Timer(3, f)
print(datetime.datetime.now().time())