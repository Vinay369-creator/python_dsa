class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        val=''
        current=self.head
        while current:
            val+= str(current.data) +' '
            current=current.next
        return val
    
    def enqueue(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def dequeue(self):
        if self.isempty():
            return 'queue is empty'
        else:
            val=self.head
            if self.head == self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
        return val 
        
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False
    def peek(self):
        if self.empty():
            return 'queue is empty'
        else:
            curr=self.head
            return curr
        
q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.dequeue())
print(q1.isempty())
print(q1.peek())
print(q1)
