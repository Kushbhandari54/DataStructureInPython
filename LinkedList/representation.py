class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end=" ")
            temp=temp.next
    
#linked list with 3 nodes
   
if __name__=="__main__":
    first=Node(10)
    second=Node(20)
    first.next=second
    third=Node(30)
    second.next=third
    llist=LinkedList()
    llist.head=first
    llist.display()