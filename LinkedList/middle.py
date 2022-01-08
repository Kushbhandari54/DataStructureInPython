#Find the middle of a given linked list
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def middleList(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        print(slow.val)
    
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end=" ")
            temp=temp.next
        return 


if __name__=="__main__":
    llist=LinkedList()
    a=Node(10)
    b=Node(20)
    a.next=b
    c=Node(30)
    b.next=c
    d=Node(40)
    c.next=d 
    e=Node(50)
    d.next=e 
    f=Node(60)
    e.next=f
    llist.head=a
    #llist.display()

    llist.middleList() 