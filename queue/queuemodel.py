# We can create the queue by using queue module
# Inside this module it contains an Queue class which is used to create the queue
# Methods avaliable in Queue class
# 1. maxsize --> used to set the size of the queue
# 2. put --> used to add the element at the last element and return the delete element
# 3. get --> used to delete the first element and return the delete element
# 4. full --> returns True if the queue is filled with exact length that specified else returns False
# 5. empty --> return True if the queue is empty else returns False

import queue 

customqueue=queue.Queue(maxsize=3)
customqueue.put(1)
customqueue.put(2)
customqueue.put(3)
print(customqueue.get())
print(customqueue.full())
print(customqueue.empty())
print(customqueue.get())