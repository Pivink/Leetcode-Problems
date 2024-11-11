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
    def remove_duplicate(self,head):
        dummy=Node(0)
        dummy.next=head
        prev=dummy
        current=head
        while current:
            if current.next and current.data==current.next.data:
                while current.next and current.data==current.next.data:
                    current=current.next
                current=current.next
                prev.next=current
            else:
                current=current.next
                prev=prev.next
        return dummy.next
l=linkedlist()
l.insert_end(1)
l.insert_end(2)
l.insert_end(3)
l.insert_end(3)
l.insert_end(4)
l.insert_end(4)
l.insert_end(5)
l.traverse()
print()
l.head=l.remove_duplicate(l.head)
l.traverse()