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
        val=[1,2,3,4] # [int(i) for i in input().split()]
        for i in val:
            newNode=Node(i)
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
        if self.head is None:
            return 'None'
        val=self.head.data
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
            if current.data==val:
                break

    def removeFirstNode(self):
        if self.head is None:
            return 'no nodes'
        else:
            self.head=self.head.next
            self.tail.next=self.head
            self.length-=1

    def removeLasttNode(self):
        if self.length==1 or self.head.next is None:
                self.head=None
                self.tail=self.head
        else:
            current=self.head
            while  current.next != self.tail:
                current=current.next
            self.tail=current
            self.tail.next=self.head
        self.length-=1 

    def removeSpecificNode(self,ip):
        if ip>=self.length:
            print('index of range')
            return 
        elif ip==0:
            self.head=self.head.next
            self.tail.next=self.head
            
        elif ip==self.length-1:
            cnode=self.head
            while cnode.next !=self.tail:
                cnode=cnode.next
            self.tail=cnode
            self.tail.next=self.head
        else:
            #c=0
            current=self.head
            # while current is not None  and c<ip-1:
            for _ in range(ip-1):
                current=current.next
                # c+=1
            current.next=current.next.next          
        self.length-=1
    
    def removeAllNodes(self):
        self.head=None
        self.tail.next=None
        self.tail=None
        self.length=0

c1=CircularList()
c1.insertNode() 
#c1.removeFirstNode()
#c1.removeLasttNode()
c1.removeSpecificNode(2)
c1.removeAllNodes()
c1.display()
print('this is length ',c1.length)