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
        val=[1,2,3,4] #[int(i) for i in input().split()]
        for n in val:
            newNode=Node(n)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                self.tail.next=self.head
            else:
                self.tail.next=newNode
                newNode.pre=self.tail
                self.tail=newNode
                self.tail.next=self.head
                self.head.pre=self.tail
            self.length+=1

    def fromHead(self):
        current=self.head
        data=self.head.data
        while current:
            print(current.data,end='->')
            current=current.next
            if data==current.data:
                break

    def fromTail(self):
        temp=self.tail
        c=self.tail.data
        while temp:
            print(temp.data,end='->')
            temp=temp.pre
            if c==temp.data:
                break

dc1=DoublyCircular()
dc1.insertNode()
#dc1.fromHead()
dc1.fromTail()
