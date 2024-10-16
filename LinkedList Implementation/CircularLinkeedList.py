class Node:
    def __int__(self,data=None,ref=None):
        self.data=data
        self.ref=ref
class CLL:
    def __init__(self,last):
        self.last=last
    def is_empty(self):
        return self.last == None
    def insert_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.ref=n
            self.last=n
        else:
            n.ref =self.last.ref
            self.last.ref=n
    def insert_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.ref = n
            self.last = n
        else:
            n.ref=self.last.ref
            self.last.ref = n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.ref
        while temp != self.last:
            if temp.data==data:
                return data
            temp=temp.next
        if temp.data == data:
            return temp
        return None
    def insert_after(self,newdata,temp):
        if temp is not None:
            n=Node(newdata,temp.ref)
            temp.ref=n
            if temp==self.last:
                self.last=n
    def print_list(self):
            if not self.is_empty():
               temp=self.last.ref
            while temp!=self.last:
                print(temp.data)
                temp=temp.ref
            print(temp.ref)
    def delete_first(self):
        if not self.is_empty():
            if self.last.ref==self.last:
                self.last=None
            else:
                self.last.ref=self.last.ref.ref
    def delete_last(self):
        if not self.is_empty():
            if self.last.ref == self.last:
                self.last = None
            else:
                temp=self.last.ref
                while temp.ref != self.last:
                     temp=temp.ref
                temp.ref=self.last.ref
                self.last=temp
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.ref==self.last:
                if self.last.data==data:
                    self.last=None
            else:
                if self.last.ref==data:
                    self.delete_first()
                else:
                    temp=self.last.ref
                    while temp !=self.last:
                        if temp.ref ==self.last:
                             if self.last.data==data:
                                 self.delete_last()
                             break
                        if temp.ref.data==data:
                            temp.ref=temp.ref.ref
                            break
                        temp=temp.ref










