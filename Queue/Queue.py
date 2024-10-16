class Queue:
    def __init__(self):
        self.items=[]
        self.front=None
        self.rear=None
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('Queue is Empty or UnderFlow')
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Queue is Empty or UnderFlow')
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Queue is Empty or UnderFlow','ok')
    def size(self):
        return len(self.items)

q1=Queue()
# print(q1.get_front())
try:
    print('Front_Elelment:',q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
try:
    q1.dequeue()
    print(q1.size())
except IndexError as e:
    print(e.args[0])




