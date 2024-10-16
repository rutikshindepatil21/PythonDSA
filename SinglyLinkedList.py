class Node:
    def __init__(self,data=None,ref=None):
        self.data=data
        self.ref=ref
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head
    def is_Empty(self):
        # if self.head==None:
            return self.head==None
            # return True
    def insert_at_Start(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    def insert_at_Last(self,data):
        new_node=Node(data)
        if not self.is_Empty():
            temp=self.head
            while temp.ref is not None:
                temp=temp.ref
            temp.ref = new_node
        else:
            self.head=new_node


        while temp != None:
            if temp.data==data:
                return temp
            temp=temp.ref
        return None
    def insert_after(self,data,newdata):
        temp=self.head
        while temp != None:
            if temp.data==data:
                new_node=Node(newdata,temp.ref)
                temp.ref=new_node
            temp=temp.ref

    def print_list(self):
        temp=self.head

        while temp is not None:
            print(temp.data,end='->')
            temp=temp.ref


    def delete_first(self):
        if self.head != None :
             self.head = self.head.ref

    def delete_last(self):
        if self.head==None:
            pass
        elif self.head.ref == None:
            self.head=None
        else:
            temp=self.head
            while temp.ref.ref != None:
                temp=temp.ref
            temp.ref=None
    def delete_item(self,data):
        if self.head is None:
            pass
        elif self.head.ref==None:
            if self.head.data==data:
                self.head=None
        else:
          temp=self.head
        if temp.data == data:
                self.head=temp.ref
        else:
            while temp.ref != None:
                    if temp.ref.data==data:
                        temp.ref = temp.ref.ref
                        break
                    temp=temp.ref
        def __iter__(self):
            return SLLIterable(self.head )

class SLLIterable:
    def __init__(self,head):
        self.head=head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.head:
            raise StopIteration
        data=self.head.data
        self.head=self.head.ref
        return data




# my_lst=SinglyLinkedList()
# my_lst.insert_at_Start(23)
# my_lst.insert_at_Start(10)
# my_lst.insert_at_Start(120)
# my_lst.insert_at_Start(103)
# my_lst.insert_at_Start(101)
# my_lst.insert_at_Start(108)
# # my_lst.insert_after(23,16)
# # my_lst.insert_after(23,67)
# my_lst.insert_at_Last(90)
# print(my_lst.print_list())
# my_lst.delete_item(101)
# # my_lst.delete_first()
# # my_lst.delete_last()
#
# my_lst.print_list()
# print()

