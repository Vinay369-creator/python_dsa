class Node:
    def __init__(self,value):
        self.data=value

class LinkedList():
    def __init__(self):
        self.top=None
        self.length=0

    def push(self,val):
        new_node=Node(val)
        new_node.next=self.top
        self.top=new_node
        self.length+=1

    def pop(self):
        popnode=self.top
        self.top=self.top.next
        return popnode

    def __str__(self):
        current=self.top
        val=''
        while current:
            val+=str(current.data)+ '\n'
            current=current.next
        return val
    
    def peek(self):
        peaknode=self.top
        return peaknode

    def is_empty(self):
        if self.top is None:
            return False
        else:
            return True

    def clear(self):
        self.top=None

l1=LinkedList()
l1.push(10)
l1.push(20)
l1.push(30)
l1.push(40)
print(l1.pop())
print(l1)