class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertNode(self, data):
        n1 = Node(data)
        if self.head is None:
            self.head = n1
            self.tail = n1
        else:
            self.tail.next = n1
            self.tail = self.tail.next
    
    def insertMultiple(self, values):
        for val in values:
            self.insertNode(val)
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def RemoveDuplicates(self):
    current=self.head
    while current:
        temp=current
        while temp.next is not None:
            if temp.data ==current.data:
                temp.next=temp.next.next
            else:
                temp=temp.next
            current=current.next

# l1 = LinkedList()
# l1.insertMultiple([1, 2, 3, 2, 4, 3])
# l1.display()
#--------------------------------------------------------------------------------------------
# 2->4->3
# 5->6->4
#output list 7->0->8 

# return the new Sum Node 
def sumLinkedList(l1,l2):
    n1=l1.head
    n2=l2.head
    carry=0
    tt=dummy=Node(0)
    while n1 or n2 or carry:
        res=carry
        if n1:
            res+=n1.data
            n1=n1.next
        if n2:
            res+=n2.data
            n2=n2.next

        tt.next=Node(res%10)
        carry=res//10
        tt=tt.next
    return dummy.next

# l1=LinkedList()
# l1.insertMultiple([2,4,3])
# l2=LinkedList()
# l2.insertMultiple([5,6,4])
# res=sumLinkedList(l1,l2)
# #to display the returned new list
# res_list=LinkedList()
# res_list.head=res
# res_list.display()

#--------------------------------------------------------------------------------------------
#original list
#1->2->3->4
#after swap the node
#2->1->4->3

def swapNodes(node):
    if node is None  or node.next is None:
        return node
    first=node
    second=node.next
    pair=second.next
    second.next=first
    first.next=swapNodes(pair)
    return second
       
# l1=LinkedList()
# l1.insertMultiple([1,2,3,4])
# l1.head=swapNodes(l1.head)
# l1.display()

#--------------------------------------------------------------------------------------------
#original list
#1->2->3->4->5   n=2
# after delete #1->2->3->5

def deleteNthNode(head,n):
    dummy=Node(0)
    dummy.next=head
    first=dummy
    second=dummy
    for _ in range(n+1):
        first=first.next
    while first is not None:
        first=first.next
        second=second.next
    second.next=second.next.next
    return dummy.next

# l1=LinkedList()
# l1.insertMultiple([1,2,3,4,5])
# l1.head=deleteNthNode(l1.head,2)
# l1.display()

#--------------------------------------------------------------------------------------------
#original list
# 1->2->3->4->5 
# output 3
# return the middle of the linked list if there are two nodes return the second node

def getNode(head):
    if head is None:
        return None
    first=head
    second=head
    while first.next and first.next.next is not None:
        first=first.next.next
        second=second.next 
    return second

# l1=LinkedList()
# l1.insertMultiple([1,2,3,4,5])
# ret=getNode(l1.head)
# #l1.display()
# print(ret)

#--------------------------------------------------------------------------------------------
#original list
#1->4->2->5->3
# after sort the list
# 1->2->3->4->5   
def mergeSort(head):    
    if not head or not head.next:
        return head
          
    middle = getMiddle(head)
    next_to_middle = middle.next
    middle.next = None  # Split the list into two halves     
       
    left = mergeSort(head)
    right = mergeSort(next_to_middle)  
    sorted_list = sortedMerge(left, right)
    return sorted_list
    
def getMiddle(head):
    if not head:
        return head     
    slow = head
    fast = head     
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next       
    return slow
    
def sortedMerge(a, b):
    result = None     
    if not a:
        return b
    if not b:
        return a 
    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)        
    return result
    
def sort(head):
    head = mergeSort(head)

# l1 = LinkedList()
# l1.insertMultiple([3, 4, 1, 5, 9, 2, 6])
# sort(l1.head)
# l1.display()

#-----------------------------------------------------------------------------------------------
#remove the nth node form the end of the list
#ex 1->2->3->4->5
#n=2         |
#after  1->2->3->5

def removeNthNode(head,n):
    dummy=Node(0)
    dummy.next=head
    first=dummy
    second=dummy
    for _ in range(n+1):
        first=first.next
    while first is not None:
        first=first.next
        second=second.next
    second.next=second.next.next
    return dummy.next

# l1=LinkedList()
# l1.insertMultiple([1,2,3,4,5])
# l1.head=removeNthNode(l1.head,2)
# l1.display()

#-----------------------------------------------------------------------------------------------
#return the middle node form the list
#ex 1->2->3->4->5
#output 3

def middleNode(head):
    current=head
    second=head
    while current and current.next is not None:
        current=current.next.next
        second=second.next
    return second

# l1=LinkedList()
# l1.insertMultiple([1,2,3,4,5])
# n1=middleNode(l1.head)
# print(n1.data)
