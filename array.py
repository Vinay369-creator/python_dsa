# in python we can use array in three main ways  list , array  , numpy
#going with the list as array

#basic array implementation
arr=[1,2,5,3,6,8]  
print(arr)

#searching the element based on index position
arr=[1,2,5,3,6,8]
print(arr[3])   # --> O(1) time complexity

#traversing through array
arr=[1,2,5,3,6,8]
for ele in range(len(arr)):
    print(arr[ele])  #--> log(n)

#search the specific elements
arr=[1,2,5,3,6,8,3,7]
target=6
def search(arr,target):
    for i in arr:    #-->log(n)
        if i==arr:   #-->O(1)
            return i
search(arr,target)

#remove specified elements
arr=[1,2,5,3,6,8,3,7]
target=3
def removele(arr,target):
    for i in arr:    #-->log(n)
        if i==arr:   #-->O(1)
            arr.remove(i)
removele(arr,target)
