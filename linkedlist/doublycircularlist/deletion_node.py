class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None

class DoublyCircular():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def insertNode(self):
        val=[1,2,3,4,5] #[int(i) for i in input(),split()]
        for n in val:
            newNode=Node(n)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                self.tail.next=self.head
            else:
                newNode.pre=self.tail
                self.tail.next=newNode
                self.tail=newNode
                self.tail.next=self.head
                self.head.pre=self.tail
            self.length+=1
            
    def fromHead(self):
        val=self.head.data
        current=self.head
        while current:
            print(current.data,end='-->')
            current=current.next
            if current.data==val:
                break

    def fromTail(self):
        val=self.tail.data
        current=self.tail
        while current:
            print(current.data,end='-->')
            current=current.pre
            if current.data==val:
                break
                
    def removeFirstNode(self):
        if self.head is None:
            return None
        current=self.head
        self.head=self.head.next
        self.head.pre=self.tail
        self.tail.next=self.head
        current.next=None
        current.pre=None
        self.length-=1

    def removeLastNode(self):
        if self.head is None:
            return None
        current=self.tail
        self.tail=self.tail.pre
        self.tail.next=self.head
        self.head.pre=self.tail
        current.next=None
        current.pre=None
        self.length-=1

    def removeSpecificNode(self,ip):
        if ip<0 or ip >= self.length:
            print('index out of range')
            return
        if ip==0:
            self.head=self.head.next
            self.tail.next=self.head
            self.head.pre=self.tail

        elif ip==self.length-1:
            self.tail=self.tail.pre
            self.tail.next=self.head
            self.head.pre=self.tail
        else:
            if ip<self.length//2:
                current=self.head
                for _ in range(ip):
                    current=current.next
                current.pre.next=current.next
                current.next.pre=current.pre
                current.pre=None
                current.next=None
            else:
                temp=self.tail
                for _ in range(self.length-1,ip,-1):
                    temp=temp.pre
                temp.pre.next=temp.next
                temp.next.pre=temp.pre
                temp.next=None
                temp.pre=None
        self.length-=1

dc1=DoublyCircular()
dc1.insertNode()
dc1.removeFirstNode()
dc1.removeLastNode()
dc1.removeSpecificNode(3)
dc1.fromHead()
print()
dc1.fromTail()

            
    