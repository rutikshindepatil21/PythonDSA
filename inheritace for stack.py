from SinglyLinkedList import *

class Stack(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_Empty(self):
        return super().is_Empty()
    def push(self,data):
         self.insert_at_Start(data)

         self.item_count += 1
    def pop(self):
        if not self.is_Empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError('Stack is empty')
    def peek(self):
        if not self.is_Empty():
            return self.head.data
        else:
            raise IndexError('Stack is empty')
    def size(self):
        return self.item_count



s1=Stack()
s1.push(21)
s1.push(0)
print(s1.peek())

