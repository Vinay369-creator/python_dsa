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

