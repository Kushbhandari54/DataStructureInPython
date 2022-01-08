#Find length of loop in linked list
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def lengthLoop(self):
        slow=self.head
        fast=self.head
        count=0
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next
            fast=fast.next
            if (slow==fast):
                slow=slow.next
                fast=fast.next.next
                count=1
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next.next
                    count+=1
                break
        return count
            
            
        