# basic implementation of the Singly Linked List
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
        val= [int(i) for i in input().split()]
        for ele in val:
            new_node=Node(ele)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
            self.tail=new_node
            self.count+=1
        
ss1=SinglyLinkedList()
ss1.insertNode()


            
