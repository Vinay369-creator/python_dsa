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
        #val= [1,2,2,3,3,4]  # this list for remove the duplicates in node
        #val=[1,2,3,4,5] # this list for reverse the nodes
        #val=[1,2,3,6,4,6] # this list for removes the nodes based on the given value
        val=[1,2,2,1]
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
# ex 1->2->3->4->
# after swapping : 2->1->4->3->
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
#s1=Singlylist()
#s1.insertdata()
#s1.head=swapNode(s1.head)
#s1.dis()

#-------------------------------------------------------------------------------------------------------------------------
#remove the duplicate from sorted linked list
# 1-->2--2-->3-->3-->4-->
#output  1-->2-->3-->4-->
def removeDuplicates(head):
    if head is None :
        return None
    
    current=head
    while current is not None and current.next is not None:
        if current.data==current.next.data:
            current.next=current.next.next
        else:
            current=current.next
    return head
#s1.dis()
#print('before')
#s1.head=removeDuplicates(s1.head)
#s1.dis()

#------------------------------------------------------------------------------------------
# reverse the nodes 
# ex 1-->2-->3-->4--5-->none
# after reverse : 5-->4-->3-->2-->1-->none
def reverseNodes(head):
    current=head
    pre=None
    while current is not None:
        temp_next=current.next
        current.next=pre
        pre=current
        current=temp_next
    head=pre
    return head

# s1=Singlylist()
# s1.insertdata()
# s1.head=reverseNodes(s1.head)
# s1.dis()

#--------------------------------------------------------------------------------------------------
# remove the node based on the value
#ex val=6 node : 1->2->3->6->4->6->
#after remove nodes : 1->2->3->4->

def removeNodeForGivenValue(head,val):
    current=head
    temp=dummy=Node(0)
    s=set()
    while current:
        if current.data !=val:
            s.add(current.data)
        current=current.next
    for i in s:
        n=Node(i)
        temp.next=n
        temp=temp.next
    return dummy.next

# s1=Singlylist()
# s1.insertdata()
# val=6
# s1.head=removeNodeForGivenValue(s1.head,val)
# s1.dis()
#---------------------------------------------------------------------------------------------------

#check the whether the nodes is palindrome or not
# ex 1-2-2-1->
#1-2-1
# true 
def palindrome(head):
    s=set()
    res=False
    current=head
    while current:
        if current.data  not in s:
            s.add(current.data)
        else:
            res=True
        current=current.next
    return res

s1=Singlylist()
s1.insertdata()
res=palindrome(s1.head)
print(res)
#s1.dis()




