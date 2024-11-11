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
    def min_and_max(self):
        res=[-1,-1]
        first_critial_index=None
        prev_critial_index=None
        index=1
        prev=self.head
        current=self.head.next
        while current.next:
            if (current.data>prev.data and current.data>current.next.data) or (current.data<prev.data and current.data<current.next.data):
                if prev_critial_index is not None:
                    if res[0]!=-1:
                        res[0]=min(res[0],index-prev_critial_index)
                    else:
                        res[0]=index-prev_critial_index
                else:
                    first_critial_index=index
                prev_critial_index=index
                print(res,index,first_critial_index,prev_critial_index)
            prev=current
            current=current.next
            index+=1
        if first_critial_index != prev_critial_index:
            res[1]=prev_critial_index-first_critial_index
        return res
l=Linkedlist()
for i in reversed([1,3,2,2,3,2,2,2,7]):
    l.insert_front(i)
l.traversal()
print()
print(l.min_and_max())