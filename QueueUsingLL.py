class Node:
    def __init__(self,data=None,ref=None):
        self.data = data
        self.ref = ref

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front == None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            # self.rear=n
        else:
            self.rear.ref=n
            # self.rear=n
        self.rear=n
        self.item_count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is Empty')
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.ref
        self.item_count -= 1
    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError('Queue Is Empty')
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            raise IndexError('Queue Is Empty')
    def size(self):
        return self.item_count

q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print(q1.get_front())


