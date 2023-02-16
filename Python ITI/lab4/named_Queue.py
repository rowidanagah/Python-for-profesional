#from .qeueu_exception import *;

# from Queue import Queue
# from Exceptions import QueueOutOfRangeException

class QueueOutOfRangeException(Exception):
    def __init__(self, Errormsg) -> None:
        super().__init__(Errormsg)

class Queue :
    def __init__(self):
        self._arr = []
        print("inside queue")
    
    def isEmpty(self):
        return self._arr == []
    
    def insert(self, ele):
        self._arr.append(ele)
    
    def __len__(self):
        return len(self._arr)
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Empty queue exception!!")
        return self._arr.pop(0)
    
    # def __str__(self) -> str:
    #     return self(self.__arr)


class Named_Queue(Queue):
    def __init__(self, name, size = 5) -> None:
        super().__init__()
        self.__size = size
        self.name = name
        self.named_qeue = {self.name : self._arr}
        print(self.named_qeue)
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, new_size):
        self.__size = new_size
    
    def insert(self, ele):
        if self.__size < len(self._arr):
            raise QueueOutOfRangeException("exceed size limit")
        super().insert(ele)
    
    def __str__(self) :
        return f"a named qeue with name of {self.name} and val of  {self.named_qeue[self.name]}"

named_queue = Named_Queue("first", 4)
named_queue.insert(0)
named_queue.insert(0)
named_queue.insert(1)
named_queue.insert(2)
print(named_queue._arr)
print(named_queue)

named_queue.pop()
print(named_queue)

        


    