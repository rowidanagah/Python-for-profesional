import logging
import threading
import time


"""
   This will worke with two threads: 
    the main thread and one you started with the threading.Thread object.
"""
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    """
    `.join()` is used to make main thread  pause and
         wait for the thread x to complete running
    """
    x.join()
    logging.info("Main    : all done")



