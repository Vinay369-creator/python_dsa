# we already know to implement the basic Linked list
# now traversal through the list and adding node at first 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    
    def insertNode(self):
        val=[ int(i) for i in input().split()]
        for ele in val:
            new_node=Node(ele)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
            self.tail=new_node
            self.count+=1

    # Traversal through the Node
    def TraversalNode(self):
        current=self.head
        while current is not None:
            print(current.data,end='-->')
            current=current.next
        print('None')
    
     #add the Node at First
    def addNodeFirst(self,val):
        new_Node=Node(val)
        if self.head is None:
            self.head=new_Node
            self.tail=new_Node
        else:
            new_Node.next=self.head
            self.head=new_Node
        self.count+=1

    #add the Node at Last
    def addNodeLast(self,val):
        new_Node=Node(val)
        if self.head is None:
            self.head=new_Node
            self.tail=new_Node
            self.count+=1
            return 
        else:
            current= self.head
            while current.next is not None:
                current=current.next
            current.next=new_Node
            self.count+=1
            return            

    def addSpecificIndex(self,ip,val):
        new_Node=Node(val)

        if self.head is None:
            self.head=new_Node
            self.tail=new_Node
            self.count+=1
            return
        elif ip==0:
            new_Node.next=self.head
            self.head=new_Node
            return 

        else:
            c=0
            current=self.head
            while current.next is not None and c<ip-1:
                current=current.next
                c+=1
            new_Node.next=current.next
            current.next=new_Node

ss1=SinglyLinkedList()
ss1.insertNode()
ss1.addSpecificIndex(3,50)
ss1.addNodeLast(70)
ss1.addNodeFirst(8)
ss1.TraversalNode()
            
