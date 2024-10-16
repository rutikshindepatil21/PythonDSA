class Deque:
    def __init__(self):
        self.items=[]
        self.item_count=0
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return self.item_count
    def insert_front(self,data):
        # inserting element at front position or end of the deque
        self.items.insert(0,data)
    def insert_rear(self,data):
        # inserting at element rear position
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('Deque is Empty')

    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError('Deque is Empty')

        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Deque is Empty')
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Deque is Empty')
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Deque is Empty')
d=Deque()
d.insert_rear(2)
d.insert_front(4)
d.insert_front(9)
d.insert_front(0)
print(d.get_front())










