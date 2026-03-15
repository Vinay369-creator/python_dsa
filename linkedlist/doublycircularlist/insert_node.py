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
        val=[1,2,3,4,5] #[int(i) for i in input().split()]
        for n in val:
            newNode=Node(n)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                self.head.pre=self.tail
                self.tail.next=self.head
            else:
                self.tail.next=newNode
                newNode.pre=self.tail
                self.tail=newNode
                self.tail.next=self.head
                self.head.pre=self.tail
            self.length+=1

    def fromHead(self):
        c=self.head
        d=self.head.data
        while c:
            print(c.data,end='->')
            c=c.next
            if c.data==d:
                break

    def fromTail(self):
        c=self.tail
        d=self.tail.data
        while c:
            print(c.data,end='->')
            c=c.pre
            if c.data==d:
                break

    def insertFirst(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
            self.head.pre=self.pre
            return
        else:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode
            self.tail.next=self.head
            self.head.pre=self.tail
        self.length+=1

    def insertLast(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.tail.next=self.head
            self.head.pre=self.tail
            return
        else:
            self.tail.next=newNode
            newNode.pre=self.tail
            self.tail=newNode
            self.tail.next=self.head
            self.head.pre=self.tail
            # newNode.pre=self.tail
            # self.tail=newNode
            # self.tail.next=self.head
        self.length+=1

    def insertSpecific(self,ip,data):
        newNode=Node(data)
        if ip<0 or ip >=self.length:
            print('index out of range')
            return None
        if ip==0:
            newNode.next=self.head
            self.head.pre=newNode
            self.head=newNode
            self.tail.next=self.head
            self.head.pre=self.tail

        elif ip==self.length-1:
            newNode.next=self.tail
            newNode.pre=self.tail.pre
            self.tail.pre.next=newNode
            self.tail.pre=newNode

        else:
            current=self.head
            c=0
            while current and c<ip:
                current=current.next
                c+=1
            newNode.next=current
            newNode.pre=current.pre
            current.pre.next=newNode
            current.pre=newNode
        self.length+=1

    def getNode(self,ip):
        if ip<0 or ip>=self.length:
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

    def searchNode(self,data):
        current=self.head
        c=0
        while c<=self.length:
            if data==current.data:
                return True
            c+=1
            current=current.next
        return False
                  
dc1=DoublyCircular()
dc1.insertNode()
#dc1.insertFirst(30)
#dc1.insertLast(30)
# print(f'length of the nodes {dc1.length-1}')
# dc1.insertSpecific(4,444)
dc1.fromHead()
# print()
# dc1.fromTail()
# print(f'length of the nodes {dc1.length}')
#print(dc1.searchNode(13))
vv=dc1.getNode(5)