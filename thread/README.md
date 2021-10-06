## Thread 

Thread is a basic unitof CPU Utlization.

A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).

A thread contains all this information in a Thread Control Block (TCB):
   - Thread Identifier: Unique id (TID) is assigned to every new thread
   - Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
   - Program counter: a register which stores the address of the instruction currently being executed by thread.
   - Thread state: can be running, ready, waiting, start or done.
   - Thread’s register set: registers assigned to thread for computations.
   - Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.


One process can have Multiple threads where:
	- Each thread has its own __Register set__ and __loacal vals__.
	- Shared __global variables__ (stored in heap) and the __program code__. 

![](https://media.geeksforgeeks.org/wp-content/uploads/multithreading-python-21.png)


Thread is a separate flow of execution. This means that your program will have two things happening at once. But for most Python 3 implementations the different threads do not actually execute at the same time: they merely appear to.



---

__Threading__  module provides a very simple and intuitive API for implementing multiple threads.

Python threads are used in cases where the execution of a task involves some waiting. 

One example would be interaction with a service hosted on another computer, such as a webserver.

> Note : Because of the way CPython implementation of Python works, threading may not speed up all tasks. This is due to interactions with the GIL that essentially limit one Python thread to run at a time



To create a new thread is by calling `threading.Thread`.

```python

from threading import Thread

def foo():
	print ("Hola Hola")

"""

Syntax :: Thread(target , args), where :

	- target: refere to the function to be run.
	- args: the arguments to be passed to the target function
"""
f1 = Thread(target = foo)
# the thread will never be excuted unless `start` is called
f1.start()

```

> Start will run and terminated.
 
 Calling `thread_name.start` again will cuase a `RuntimeError`



## Working With Many Threads

Multiple Threads programm mechanism will be the same as the above code example,
firstly it's required to create thread objects, then call `.start()` for eachthread obj and use `.join()` to make each thread complete its task before excuting another thread.

Multiple runs for a programm that contains Multiple Threads will produce different orderings, it depends on the OS and quit hard to predict the proper ordering or excuting the threads.However Python provide.



## Resources

- [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
- [Notes on threading DEV.io post](https://dev.to/samueleresca/notes-on-threading-1cnm)
- [Python-threading Real Python](https://realpython.com/intro-to-python-threading/#what-is-a-thread)
- [Notes on Thread and threading module in python DEV.io posted by me]()
- [How to implement Python stack `To read`](https://realpython.com/how-to-implement-python-stack/)