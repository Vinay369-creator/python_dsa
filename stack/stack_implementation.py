# Stack it is the one of the In computer science and data structures, a "stack" is a fundamental and widely 
# used linear data structure that follows the Last-In-First-Out (LIFO) principle. 
# This means that the last item added to the stack is the first one to be removed. 
# Think of it as a collection of items stacked on top of each other, where you can only add or remove items from the top.

#Key operations associated with a stack data structure are:
#Push: This operation adds an item to the top of the stack.
#Pop: This operation removes and returns the item from the top of the stack.
#Peek (or Top): This operation retrieves the item from the top of the stack without removing it.
#Is Empty: Checks whether the stack is empty.

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,ele):
        self.items.append(ele)

    def __str__(self):
        if len(self.items) <1:
            return False
        val=''
        for i in self.items[::-1]:
            val+=str(i) + '\n'    
        return val
    
    def pop(self):
        if len(self.items)<1:
            return False
        popval=self.items.pop()
        print(popval)
        return popval

    def peek(self):
        peakval=self.items[-1]
        print(peakval)
        return peakval

mystack=Stack()
mystack.push(10)
mystack.push(20)
mystack.push(30)
#print(mystack)

