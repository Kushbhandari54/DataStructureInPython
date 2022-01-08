#Function to check if a singly linked list is palindrome
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def palindromeLinkedList(self):
        temp=self.head
        lst=[]
        while(temp!=None):
            lst.append(temp.val)
            temp=temp.next
        
        temp=self.head
        while(temp!=None):
            a=lst.pop()
            if a!=temp.val:
                return False
            temp=temp.next
        return True
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end=" ")
            temp=temp.next

if __name__=="__main__":
    llist=LinkedList()
    a=Node(1)
    b=Node(2)
    a.next=b
    c=Node(3)
    b.next=c
    d=Node(2)
    c.next=d
    e=Node(1)
    d.next=e

    llist.head=a
    print(llist.palindromeLinkedList())
    llist.display()