class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularList():
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insertNode(self):
        val= [1,2,3,4] #[int(i)  for i in  input().split()]
        for n in val:
            newNode=Node(n)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                newNode.next=self.head
            else:
                self.tail.next=newNode
                newNode.next=self.head
            self.tail=self.tail.next

c1=CircularList()
c1.insertNode()

