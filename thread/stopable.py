import threading
import time


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

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()
    def stop(self):
        self._stop_event.set()

    def join(self, *args, **kwargs):
        self.stop()
        super(StoppableThread,self).join(*args, **kwargs)
    
    def run():
        while not self._stop_event.is_set():
            print("Still running!")
            time.sleep(2)


print("stopped!")