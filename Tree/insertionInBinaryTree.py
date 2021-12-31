class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insertion(root,data):
    new_node=Node(data)
    if root==None:
        root=new_node
    
    queue=[]
    queue.append(root)
    while(len(queue)!=0):
        a=queue.pop(0)
        if a.left==None:
            a.left=new_node
            break
        else:
            queue.append(a.left)

        if a.right==None:
            a.right=new_node
            break
        else:
            queue.append(a.right)

def inorder(temp):
    if temp==None:
        return 
    inorder(temp.left)
    print(temp.data,end=' ')
    inorder(temp.right)

root=Node(10)
insertion(root,10)
insertion(root,20)
insertion(root,30)
insertion(root,40)
insertion(root,50)
inorder(root)