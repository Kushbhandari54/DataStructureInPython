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

    def display(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next


if __name__=='__main__':
    llist=LinkedList()
    llist.insertion(10)
    llist.insertion(20)
    llist.insertion(30)
    llist.display()