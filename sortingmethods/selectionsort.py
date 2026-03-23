# it will sort the least elements from 0 index position and it compares with the all the elements 
# after comparing with elements lastly it swaps the least element with that particular element.

#l[3,1,6,9]
# first it starts with the 0 index position which is 3 it compares with the all elements and 
# which element is least after comparision it  swap the least element with the particular index position
 

# algorithm for the sorting the elements in ascending order.
l=[5,3,22,0,68,-5]

for ind1 in range(len(l)-1):
    least=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[ind2] < l[least]:
            least=ind2

    l[ind1],l[least]=l[least],l[ind1]

#print(l)

# algorithm for the sorting the elements in the descending order 
l=[5,3,22,0,68,-5]
for ind1 in range(len(l)-1):
    least=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[ind2]> l[least]:
            least=ind2
    l[least],l[ind1]=l[ind1],l[least]

print(l)
