#Detect loop in a linked list


class Node:
    def __init__(self,data):
        self.val=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def detectLoop(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

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
    #f.next=c
    llist.head=a
    print(llist.detectLoop())