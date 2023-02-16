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

queue = Queue()

queue.insert(2)
queue.insert(2)
print(queue.pop())

# print(queue.pop())
# print(queue.pop())