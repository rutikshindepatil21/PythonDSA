class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        return self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return 'Empty Stack'
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Empty Stack'
    def size(self):
        return len(self.items)

s1=Stack()
s1.push(23)
s1.push(23)
s1.push(23)
s1.push(23)
s1.push(23)
s1.push(23)
s1.push(23)
s1.push(2)

print(s1.pop())