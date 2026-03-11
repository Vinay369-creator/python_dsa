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
        val=[1,2,10,3,4,5]
        for i in val:
            newNode=Node(i)
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                self.tailnext=self.head
            else:
                self.tail.next=newNode
                self.tail=newNode
                self.tail.next=self.head
            self.length+=1
    def display(self):
        current=self.head
        val=self.head.data
        while current:
            print(current.data,end='->')
            current=current.next
            if current.data==val:
                break
# c1=CircularList()
# c1.insertNode()
# c1.display()

#-------------------------------------------------------------------------------------------------
# search the given node whether it is present or not.
def searchNode(head,val):
    current=head
    value=head.data
    while current:
        if current.data==val:
            return True
        current=current.next
        if value==current.data:
            break
    return False

# c1=CircularList()
# c1.insertNode()
# print(searchNode(c1.head,7))
#c1.display()

#-------------------------------------------------------------------------------------------------
# check if the Nodes is sorted or not
def isSortedNodes(head):
    if head is None:
        return True
    current=head
    while current.next !=head:
        if current.data > current.next.data:
            return False
        current=current.next
    return True

# c1=CircularList()
# c1.insertNode()
# c1.display()
# print(isSortedNodes(c1.head))

# insert the node into the sorted linked list.

def insert_Sorted_Node(head,tail,data):
    newNode=Node(data)
    if head is None:
        head=newNode
        newNode.next=head
    elif data <=head.data:
        newNode.next=head
        head=newNode
        tail.next=head
    else:
        current=head
        while current.next !=head and current.next.data < data:
            current=current.next
        newNode.next=current.next
        current.next=newNode 
        
# c1=CircularList()
# c1.insertNode()
# insert_Sorted_Node(c1.head,c1.tail,2)
# c1.display()

