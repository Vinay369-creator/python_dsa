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

#remove duplicate elements in array
arr=[1,2,5,3,6,8,3,7,2,1,8]
def removeDuplicate(arr):
    j=0
    for i in range(1,len(arr)):          #--->  time complexity O(n)
        if arr[i] !=arr[i-1]:
            arr[j]=arr[i]
            j+=1
    return arr
sortedarray=removeDuplicate(arr)
print(sortedarray)

#using another approch which constist  O(n)
def removeDuplicateSet(arr):
    arr=list(set(arr))
    return arr
sortedarray=removeDuplicateSet(arr)


arr=[1,2,5,3,6,8,3,7,2,1,8]
#search particular element using linear search 
def searchLinear(arr,target):
    for i in range(len(arr)):
       if target==arr[i]:
           return i
    return 'Not Found'
searchLinear(arr,target=7)


#search particular element using binary search 
def searchEleBinary(arr,target):
    i=0
    j=len(arr)-1
    while i<=j:
        mid=i+j//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            i=mid+1
        else:
            j=mid-1
    return 'Not Found'
target=6
retval=searchEleBinary(arr,target)

# program to write the function to get the first and second largest numbers in the array
arr=[84,66,78,93,91,55,95]
def largest(arr):
    mx=0
    mx2=0
    for no in arr:
        if no> mx:
            mx2=mx
            mx=no
        elif mx>no and no>mx2:
            mx2=no
    return mx,mx2
largest(arr)

#program to check whether array contains duplicates or not
arr[3,5,4,6,7,3,2,1,3,2]
def isduplicate(arr):
    for no in range(len(arr)-1):
        if arr[no] in arr[no+1:]:
            return True
    else:
        return False
def duplicate(arr):
    if isduplicate(arr):
        print('yes it contains the duplicates')
    else:
        print('no its not contains the duplicates' )



