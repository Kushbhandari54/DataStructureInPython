class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class LinkedList:
    def __init__(self):
            self.head=None

    #insertion at the end of linked list
    def insertion(self,data):
        new_node=Node(data)                          #creating of a new node
        if self.head==None:
            self.head=new_node
            return 

        temp=self.head
        while(temp!=None and  temp.next!=None):
            temp=temp.next
        temp.next=new_node
        return self.head

    def Deletion(self):
        #to delete the first node
        if self.head==None:
            return 
        self.head=self.head.next
        
        #to delete the last node
        temp=self.head
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        

    def display(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next
