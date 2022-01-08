#Remove duplicates from a sorted linked list
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return 
        temp=self.head
        while(temp!=None and temp.next!=None):
            temp=temp.next
        
        temp.next=new_node

    def removeDuplicate(self):
        i=self.head
        j=self.head.next
        while(j!=None):
            if i.val==j.val:
                i.next=j.next
                j=i.next
            else:
                i=i.next
                j=j.next
        return self.head

    
    def display(self):
        temp=self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next


if __name__=="__main__":
    llist=LinkedList()
    llist.push(11)
    llist.push(11)
    llist.push(11)
    llist.push(21)
    llist.push(43)
    llist.push(43)
    llist.push(60)

    llist.display()
    print("")
    llist.removeDuplicate()
    llist.display()