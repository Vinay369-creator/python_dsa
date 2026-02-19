#two dimensional array.
# find the target element in the given 2d array and return the  index position of the element 
arr=[[1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]]
target = 3

def targetElement(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return i,j
    return 'Not found'
print(targetElement(arr,target))

#rotate the matrix/image
#ex arr[[1,2,3],             arr =[[7,4,1],
     #  [4,5,6],                  [8,5,2],
     #  [7,8,9]]                  [9,6,3]]

arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]

def rotatearr(arr):
    for row in range(len(arr)):
        for col in range(row,len(arr)):
            arr[row][col],arr[col],[row]=arr[col],[row],arr[row],[col]
    
    for k in arr:
        k.reverse()
    return arr
print(rotatearr(arr))

#calculate the sum of the diagonal element
#ex arr=[[1,2,3],
        #[4,5,6],
        #[7,8,9]]

#  in  the arr diagoinal which means in 1st row the 1st element and in 2nd row 2nd element and 3rd row 3rd element
#so the selected elements are 1 , 5, 9, == total sum of the all numbers is 15
def diagonalElements(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i][i]
    return total
print(diagonalElements(arr))

