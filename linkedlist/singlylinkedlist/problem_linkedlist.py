#swap the every two nodes 
#  present nodes 1-->2-->3-->4-->
# updated nodes  2-->1-->4-->3-->
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlylist():
    def __init__(self):
        self.head=None
        self.tail=None

    def insertdata(self):
        val= [1,2,2,3,3,4] 
        for i in val:
            n1=Node(i)
            if self.head is None :
                self.head=n1
                self.tail=n1
            else:
                self.tail.next=n1
                self.tail=n1 

    def dis(self):
        current=self.head
        while current is not None:
            print(current.data,end='->')
            current=current.next
#-------------------------------------------------------------------------------------------------------------------------
#logic for the swap of nodes
def swapNode(head):
    if head  is None or head.next is None :
        return head
    first=head
    second=head.next
    pairnodes=second.next
    second.next=first
    first.next=swapNode(pairnodes)
    print(second.data)
    return second
s1=Singlylist()
s1.insertdata()
s1.head=swapNode(s1.head)
s1.dis()

#-------------------------------------------------------------------------------------------------------------------------
#remove the duplicate from sorted linked list
# 1-->2--2-->3-->3-->4-->
#output  1-->2-->3-->4-->
def removeDuplicates(head):
    if head is None :
        return None
    
    current=head
    while current is not None and current.next is not None:
        print('compares --',current.data,current.next.data)
        if current.data==current.next.data:
            current.next=current.next.next
            print('after ' ,current.data)
        else:
            current=current.next
    return head
s1.dis()
print('before')
s1.head=removeDuplicates(s1.head)
s1.dis()



