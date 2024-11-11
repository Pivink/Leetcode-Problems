class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def preorder(self,n):
        print(n.data,"-->",end=" ")
        if(n.left):
            self.preorder(n.left)  
        if(n.right):
            self.preorder(n.right)  
    def postorder(self, n):

        if n.left:
            self.postorder(n.left)
        if n.right:
            self.postorder(n.right)
        print(n.data, "-->", end=" ")
    def inorder(self, n):
        if n.left:
            self.inorder(n.left)
        print(n.data, "-->", end=" ")
        if n.right:
            self.inorder(n.right)
    def insert(self,data):
        if(self.root == None):
            self.root=Node(data)
        else:
            new=Node(data)
            n=self.root
            while(n!=None):
                prev=n
                if(data == n.data):
                    return
                elif(data > n.data):
                    n=n.right
                else:
                    n=n.left
            if(data>prev.data):
                prev.right=new
            else:
                prev.left=new
    def hight(self, node):
        if node is None:
            return -1
        return max(self.hight(node.left), self.hight(node.right)) + 1
    def ipre(self,root):
        if(root.left):
            root=root.left
            while(root.right is not None):
                root=root.right
        elif(root.right):
            root=root.right
            while(root.right is not None):
                root=root.right
        return root
    def delete(self,root,val):
        if(root == None):
            return root
        if(root.left==None and root.right==None):
            return None
        if(val<root.data):
            root.left=self.delete(root.left,val)
        elif(val>root.data):
            root.right=self.delete(root.right,val)
        else:
            ipe=self.ipre(root)
            root.data=ipe.data
            if root.left:
                root.left=self.delete(root.left,ipe.data)
            elif root.right:
                root.right=self.delete(root.right,ipe.data)
        return root
    def path_sum(self,root,targetSum):
        def backtrack(node, current_sum):
            if not node:  
                return False
            current_sum += node.data
            print(current_sum)
            if not node.left and not node.right:
                return current_sum == targetSum
            return (backtrack(node.left, current_sum) or
                    backtrack(node.right, current_sum))
        return backtrack(root,0)
tree=BST()
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
tree.insert(5)
tree.insert(4)
tree.insert(8)
tree.insert(13)
tree.insert(4)
tree.insert(7)
tree.insert(1)
tree.inorder(tree.root)
print()
print(tree.path_sum(tree.root,26))