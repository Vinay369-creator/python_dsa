class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def insertdata(self):
        val=[int(i) for i in input().split()]
        for ele in val:
            new_node=Node(ele)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
            self.tail=new_node
            self.count+=1
    
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end='-->')
            current=current.next

    def delFirstNode(self):
        if self.head is None:
            return 'None'
        self.head=self.head.next
    
    def delLastNode(self):
        if self.head is None:
            return "None"     
        current=self.head
        while current.next.next is not None:
            current=current.next
        current.next=None

    def delIndexPos(self,ip):
        if ip==0:
            self.head=self.head.next
            return 
        c=0
        current=self.head
        while current.next.next is not None and c<ip-1:
            current=current.next
            c+=1
        current.next=current.next.next
    
s1=SinglyLinkedList()
s1.insertdata()
s1.delFirstNode()
s1.delLastNode()
s1.delIndexPos(5)
s1.display()

    