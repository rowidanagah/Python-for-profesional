Which Implementation Should You Use for Stacks In Python?


## Python Stacks and Threading

Let me just recap what I've read about how to implement Stacks in python so far.

There are 2 options to create a stack in python whether using lists and deques and both of them behave differently if your program has threads.

It's a better sweet not to use lists to implement Stacks or any data structure that can be accessed by multiple threads as lists is not thread-safe. List can potentially have memory reallocation issues and it makes you build the entire functionality of the stacks on your own.


`deaues` is a thread-safe more than list, even if it's more complex than lists, according to [queue class documentation](https://docs.python.org/3/library/queue.html), it clearly states that both the `.append()`and `.pop()` operations are atomic, meaning that they won’t be interrupted by a different thread.

```language
So, while it’s possible to build a thread-safe Python stack 
using a deque, doing so exposes yourself to someone misusing
 it in the future and causing race conditions.

```

For this use [`LifoQueue`](https://docs.python.org/3/library/queue.html) from __queue__ module.


`LifoQueue` is designed to be fully thread-safe. All of its methods are safe to use in a threaded environment. 

EX
```python
from queue import LifoQueue
myStack = LifoQueue()

myStack.put('a')
myStack.put('b')
myStack.put('c')

myStack


myStack.get()

myStack.get()

myStack.get()


# myStack.get() <--- waits forever
myStack.get_nowait()

```




> In notes :
  - Use a deque if you’re not using threading.
  - If your program has threads, then you should use a LifoQueue
  - The interface of both list and deque are the same ,yet deque doesn’t have memory allocation issues, which makes deque the best choice for your non-threaded Python stack.