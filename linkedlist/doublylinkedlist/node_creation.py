class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None

class DoublyList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0  

    def insertNode(self):
        val=[1,2,3,4] # [int(i) for i in input().split()]
        for i in val:
            newNode=Node(i)   #creates the new node every time
            if  self.head is None:
                self.head=newNode
                self.tail=newNode
            else:
                self.tail.next=newNode
                newNode.pre=self.tail
                self.tail=newNode
            self.length+=1
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end='-->')
            current=current.next
d1=DoublyList()
d1.insertNode()
d1.display()

                