import threading
import time

"""
https://stackoverflow.com/questions/47912701/python-how-can-i-implement-a-stoppable-thread
"""

"""
Why not to kill a thread?
    - the thread is holding a critical resource that must be closed properly
    - the thread has created several other threads that must be killed as well.
"""
class StoppableThread(threading.Thread):
    """
    Thread class with a stop() method. The thread itself has to check
         regularly for the stopped() condition.
    """

    """
    def __init__(self):
                    super(StoppableThread, self).__init__()
                    self._stop_event = threading.Event()
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):

        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        """
        you should call stop() on the thread when you want it to exit, 
        and wait for the thread to exit properly using join()
        """
        super(StoppableThread,self).join(*args, **kwargs)
    
    def run(self):
        while not self._stop_event.is_set():
            print("Still running!")
            time.sleep(2)

import threading
import time
"""
def example():
    x = 0
    while x < 5:
        print("Hello")
        x = x + 1


t = threading.Thread(target=example)
t.start()
t.join()
"""
def funct():
    while not current_thread().stopped():
        time.sleep(1)
        print("Hello")

testthread = StoppableThread(target=funct)
testthread.start()
testthread.stop()
print("stopped!")