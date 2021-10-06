This post encompasses some notes about thread and 
__Threading__  module in python, that I used as a quick recap.

## What is Thread.
__Thread__ Is a basic unit of CPU Utlization, the smallest unit of processing that can be performed in an OS and an entity within a process. One process can have Multiple threads.


## What thread contains?

It contains specific information in a Thread Control Block (TCB) such as :
  - Thread ID which is assign to every new thread.

  - Stack pointer that contains the local variables under thread’s scope.

  - Program counter Or Register that contains the address of the current instruction being excuted by the Tthread.

  - Parent Process Pointer to point to Process control block 
  __(PCB)__ of the parent process that this thread lives on.




__Threading__  module provides a very simple and intuitive API for implementing multiple threads. *Thread* in this module encapsulates threads and provide an interface to workwith them.

To create a new thread is by calling `threading.Thread` to make an instance and then tell it to `.start()`:



```python

from threading import Thread

def foo():
  print("Hola Hola")

f1 = Thread(target = foo)
# the thread will never be excuted unless `start` is called
f1.start()
```
> Note Start will run and terminated. Calling `thread_name.start` again will cuase a 
`RuntimeError`






 [You can find the code on the following repository](https://github.com/Rowida46/Python-for-profesional/tree/main/thread), this repo is a chapter in a [Python for profesional Book repo](https://github.com/Rowida46/Python-for-profesional).


