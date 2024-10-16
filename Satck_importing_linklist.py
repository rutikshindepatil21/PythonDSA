from SinglyLinkedList import *

class Stack:
    def __init__(self):
        self.mylist=SinglyLinkedList()
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_Empty()
    def push(self,data):
        self.mylist.insert_at_Start(data)
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count -= 1
    def peek(self):
        if not self.is_empty():
            return self.mylist.head.data
    def size(self):
        return self.item_count
s1=Stack()
s1.push(21)
s1.push(78)
s1.push(70)
s1.push(8)
s1.push(65)
print(s1.peek())

print(s1.item_count)




