class Node:
    def __init__(self,prev=None,data=None,ref=None):
        self.prev=prev
        self.data=data
        self.ref=ref
class Dll:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        return self.head==None
    def insert_first(self,data):
        n = Node(data=data)
        if not self.is_empty():
            n.prev=self.head.ref
            n.ref=self.head
        self.head=n
    def insert_last(self,data):

        temp=self.head
        n = Node(temp, data=data)
        if self.head !=None:
            while temp.ref != None:
                temp=temp.ref

            if self.head==None:
                self.head=n
            else:
                temp.ref = n

    def search(self,data):
        temp=self.head
        while temp != None:
            if temp.data==data:
                  return temp
            temp=temp.ref
        return None
    def insert_after(self,temp,data):
        if temp != None:
            n=Node(temp,data,temp.ref)
            if temp.ref != None:
                temp.ref.prev=n
            temp.ref=n

    def print_list(self):
        temp=self.head
        while temp != None:
            print(temp.data,end=' <-> ')
            temp=temp.ref
    def delete_first(self):
        if self.head is not None:
            self.head=self.head.ref
            if self.head is not None:
                self.head.prev=None
    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.ref is None:
            self.head=None
        else:
            temp=self.head
            while temp is not None:
                temp=temp.ref
            temp.prev.ref=None
    def delete_item(self,data):
        if self.head is  None:
            pass
        else:
            temp = self.head
            while temp is not None:
                if temp.data==data:
                    if temp.ref is not None:
                        temp.ref.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.ref = temp.ref
                    else:
                        self.head=temp.ref
                    break
                temp=temp.ref

db=Dll()
db.insert_first(20)
db.insert_first(98)
db.insert_first(940)
db.insert_first(80)
db.insert_after(db.search(98),23)
db.insert_after(db.search(23),83)
db.delete_item(83)
db.print_list()


