class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front == None
    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n
        self.front=n
    def insert_rear(self,data):
        n=Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.front=n
    def delete_front(self):
        if self.is_empty():
            raise IndexError('the que is empty')
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front = self.front.next
            self.front.prev = None

    def delete_rear(self):
        if self.is_empty():
            raise IndexError('the que is empty')
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
