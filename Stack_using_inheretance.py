class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
             super().pop()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('stack is empty')
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError('no attribute')
s1=Stack()
s1.push(23)
s1.push(24)
s1.push(25)
s1.push(26)
print(s1)
print(type(
    s1
))