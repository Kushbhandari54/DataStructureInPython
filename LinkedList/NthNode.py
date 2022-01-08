#Write a function to get Nth node from end in a Linked List

class Node:
    def __init__(self,data):
        self.val=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next

    def getNthNode(self,n):
        slow=self.head
        fast=self.head
        while(n>0):
            fast=fast.next
            n-=1
        
        while(fast!=None):
            slow=slow.next
            fast=fast.next
        return slow.val
if __name__=="__main__":
    llist=LinkedList()
    first=Node(10)
    second=Node(20)
    first.next=second
    third=Node(30)
    second.next=third
    fourth=Node(40)
    third.next=fourth
    fifth=Node(50)
    fourth.next=fifth
    sixth=Node(60)
    fifth.next=sixth

    llist.head=first
    llist.display()
    print()
    print(llist.getNthNode(4))