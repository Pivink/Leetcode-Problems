class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def Display(self):
        if not self.head:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.next
    def insert_end(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            new_node=Node(data)
            n=self.head
            while(n.next is not None):
                n=n.next
            n.next=new_node
    def Swap(self):
        if not self.head or not self.head.next:
            return self.head
        n1,n2=self.head,self.head.next
        self.head,prev=n2,n1
        while(n2):
            n1.next,n2.next=n2.next,n1
            if(n2 != self.head):
                prev.next,prev=n2,n1
            n1=n1.next
            if(not n1):
                return self.head
            n2=n1.next
    def swap_2(self,head,k):
        n=head.next
        # n=n.next 
        n.data,head.data=head.data,n.data
        return head
l1=Linkedlist()
l1.insert_end(1)
l1.insert_end(2)
l1.insert_end(3)
l1.insert_end(4)
l1.insert_end(5)
l1.Display()
print()
l2=Linkedlist()
l2.head=l2.swap_2(l1.head,2)
l2.Display()