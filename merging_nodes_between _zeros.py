class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head==None:
            print("Linked list is empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.next
    def insert_front(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def merging(self):
        p=self.head.next
        temp=self.head
        sum=0
        while p:
            if p.data==0:
                temp=temp.next
                temp.data=sum
                sum=0
            else:
                sum+=p.data
            p=p.next
        temp.next=None
        return self.head.next
l=Linkedlist()
d=[0,1,0,3,0,2,2,0]
for i in d[::-1]:
    l.insert_front(i)
l.traversal()
print()
l.head=l.merging()
# print(l.head.data)
l.traversal()