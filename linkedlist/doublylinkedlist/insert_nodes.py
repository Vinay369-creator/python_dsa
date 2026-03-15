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
        val=[1,2,3,4,5] #[int(i) for i in input().split()]
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

    def fromHead(self):
        current=self.head
        while current:
            print(current.data,end='-->')
            current=current.next

    def fromTail(self):
        current=self.tail
        while current:
            print(current.data,end='-->')
            current=current.pre

    def addNodeAtFirst(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode
        self.length+=1
    
    def addNodeAtLast(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.pre=self.tail
            self.tail=newNode
        self.length+=1
        
    def addNodeAtSpecific(self,ip,data):
        newNode=Node(data)
        if ip==0:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode
            return
        if ip==self.length-1:
            self.tail.next=newNode
            newNode.pre=self.tail
            self.tail=newNode
            return 
        
        if ip<self.length//2:
            current=self.head
            for _ in range(ip):
                current=current.next
                newNode.next=current
                newNode.pre=current.pre
                current.pre.next=newNode
                current.pre=newNode

        elif ip==self.length//2:
            c=0
            curr=self.head
            while c<ip:
                c+=1
                curr=curr.next
            newNode.next=curr
            newNode.pre=curr.pre
            curr.pre.next=newNode
            curr.pre=newNode

        else:
            temp=self.tail
            for _ in range(self.length-1,ip,-1):
                temp=temp.pre
                newNode.next=temp
                newNode.pre=temp.pre
                temp.pre.next=newNode
                temp.pre=newNode
        self.length+=1
    
d1=DoublyList()
d1.insertNode()
#d1.addNodeAtFirst(40)
#d1.addNodeAtLast(333)
d1.addNodeAtSpecific(2,444)
d1.fromHead()
print()
#d1.fromTail()