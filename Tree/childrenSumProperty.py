class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def SumProperty(root):
    pass
    

if __name__=="__main__":
    root=Node(10)
    a=Node(8)
    root.left=a
    b=Node(2)
    root.right=b
    a.left=Node(3)
    a.right=Node(5)
    b.left=Node(2)
    print(SumProperty(root))