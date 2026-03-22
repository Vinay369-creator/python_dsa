# marge sort can be perform in two ways 
# 1. Is for the half sorted list 
# 2. Is for the total unsorted list
# This merge sort is follows the divide and conqure methods and it compares the left and right list's elements
# with the main list and make changes in the main memory location

# 1. merge sort for the half list sorted

l=[1,4,6,8,13,-2,3,5,12,71]
mid=len(l) //2
left=l[:mid]
right=l[mid:]
lind,rind,mind=0,0,0
while lind<len(left) and rind < len(right):
    if left[lind] > right[rind]:
        l[mind]=right[rind]
        rind+=1
    else:
        l[mind]=left[lind]
        lind+=1
    mind+=1

while lind<len(left):
    l[mind]=left[lind]
    mind+=1
    lind+=1

while rind < len(right):
    l[mind]=right[rind]
    mind+=1
    rind+=1

print(l)

#sorting the entire list 
l=[88,3,-6,2,44,13,4,23,44]

def divide(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]
    divide(left)
    divide(right)
    conqure(l,left,right)

def conqure(l,right,left):
    i,j,mid=0,0,0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            l[mid]=left[i]
            i+=1
        else:
            l[mid]=right[j]
            j+=1
        mid+=1
    while i< len(left):
        l[mid]=left[i]
        i+=1
        mid+=1
    while j < len(right):
        l[mid]=right[j]
        j+=1
        mid+=1

divide(l)
print(l)