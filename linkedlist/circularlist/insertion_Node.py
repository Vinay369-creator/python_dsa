class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def insertNode(self):
        val= [1,2,3,4]#[int(i) for i in input().split()]
        for n  in val:
            newNode=Node(n)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                self.tail.next=self.head
            else:
                self.tail.next=newNode
                self.tail=newNode
                self.tail.next=self.head
            self.length+=1
    
    def display(self):
        val=self.head.data
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
            if current.data==val:
                break

    def insertFirst(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.tail
        else:
            newNode.next=self.head
            self.head=newNode
            self.tail.next=self.head # dont forgot to update the tail position 
        self.length+=1

    def insertLast(self,val):
        newNode=Node(val)
        if self.head is None:
            return None
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head  # dont forgot to update the tail position
        self.length+=1

    def insertSpecificPos(self,ip,val):
        newNode=Node(val)
        if ip==0:
            newNode.next=self.head
            self.head=newNode
            self.tail.next=self.head
        elif ip==self.length-1:
            c=0
            current=self.head
            while current and c<ip-1:
                current=current.next
                c+=1
            current.next=newNode
            newNode.next=self.tail
        elif ip>self.length-1:
            return 'invalid index position'
        else:
            c=0
            current=self.head
            while current and c<ip-1:
                current=current.next
                c+=1
            newNode.next=current.next
            current.next=newNode
        self.length+=1

c1=CircularList()
c1.insertNode()
c1.insertFirst(10)
c1.insertLast(80)
c1.insertSpecificPos(2,55)
c1.display()
#
# print()
#print(f'this is length of the nodes {c1.length}')