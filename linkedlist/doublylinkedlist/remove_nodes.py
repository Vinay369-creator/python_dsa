class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None

class DoublyList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def insertNode(self):
        val=[1,2,3,4]
        for i in val:
            newNode=Node(i)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
            else:
                self.tail.next=newNode
                newNode.pre=self.tail
                self.tail=newNode
            self.length+=1

    def fromHed(self):
        current=self.head
        while current:
            print(current.data,end='-->')
            current=current.next

    def fromTail(self):
        current=self.tail
        while current:
            print(current.data,end='->')
            current=current.pre

    def removeFirstNode(self):
        if self.head is None:
            return None
        else:          
            self.head=self.head.next
            self.head.pre=None
        self.length-=1

    def removeLastNode(self):
        if self.tail is None:
            return None
        else:
            self.tail=self.tail.pre
            self.tail.next=None
        self.length-=1

    def removeSpecificNode(self,ip):
        if ip<0 or ip>=self.length:
            print('index out of range')
            return 
        if self.head is None:
            return None
        if ip==0:
            #self.removeFirstNode()
            self.head=self.head.next
            self.head.pre=None

        elif ip==self.length-1:
            self.tail=self.tail.pre
            self.tail.next=None
        
        else:
            current=self.head
            for _ in range(ip):
                current=current.next

            current.next.pre=current.pre
            current.pre.next=current.next
            current.pre=None
            current.next=None
            self.length-=1

    def searchNode(self,target):
        current=self.head
        while current:
            if current.data==target:
                return True
        return False
            
    def getNode(self,ip):
        #with edge cases 
        if ip < 0 or ip >=self.length:
            return None
        if ip<self.length//2:
            current=self.head
            for _ in range(ip):
                current=current.next
        else:
            current=self.tail
            for _ in range(self.length-1,ip,-1):
                current=current.pre
        return current
        
d1=DoublyList()
d1.insertNode()
d1.removeFirstNode()
d1.removeLastNode()
d1.removeSpecificNode(4)
d1.fromHed()
print()
d1.fromTail()
retnode=d1.getNode(0)
print(retnode)