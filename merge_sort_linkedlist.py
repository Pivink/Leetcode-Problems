import time
start_time = time.time()
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.next
    def insert_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            new_node=Node(data)
            n=self.head
            while n.next:
                n=n.next
            n.next=new_node
    def merge(self,n1,n2):
        if not n1 and not n2:
            return None
        if not n1:
            return n2
        if not n2:
            return n1
        else:
            dummy=Node(0)
            c=dummy
            while n1 and n2:
                if n1.data > n2.data:
                    c.next=n2
                    n2=n2.next
                else:
                    c.next=n1
                    n1=n1.next
                c=c.next
            c.next=n1 or n2
            return dummy.next
    def mergeklist(self,list1):
        if not list1:
            return None
        if len(list1)==1:
            return list1[0]
        mid=len(list1)//2
        left=self.mergeklist(list1[:mid])
        right=self.mergeklist(list1[mid:])
        return self.merge(left,right)
    def remove_duplicate(self):
        p=self.head
        n=self.head.next
        while n:
            if p.data==n.data:
                n=n.next
                p.next=n
            else:
                n=n.next 
                p=p.next 
l=[1,2,3]
l2=[1,3]
print(l==l2)