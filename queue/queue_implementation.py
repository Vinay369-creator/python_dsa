# Queue contains the enqueue and dequeue methods which is used to insert the elements at last 
# Queue follows the FIFO princpal (First in First out)
# Queue serves for the first elements add at  first and newly addded elements at last. 
# Enque method is used to insert the elements at last
# Dequeue method is used to delete the elments from first.
# To use the queue we can use the list collection data type or python provide the moduel called Queue


# Basic implementation of Queue.
class Queue:
    def __init__(self):
        self.items=[]

    def __str__(self):
        val=''
        for i in self.items:
            val += str(i) + ' '
        return val

    def enqueu(self,element):
        self.items.append(element)
        print('new node is inserted in end of list')

    def dequeue(self):
        val=self.items.pop()
        return val

    def isempty(self):
        if self.items==[]:
            return True
        else:
            return False
        
    def first(self):
        val=self.items[0]
        return val

customqueue=Queue()
customqueue.enqueu(10)
customqueue.enqueu(20)
customqueue.enqueu(30)
customqueue.enqueu(40)
customqueue.dequeue()
customqueue.first()
customqueue.isempty()
print(customqueue)
