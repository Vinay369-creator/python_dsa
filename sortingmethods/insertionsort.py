# It is one of the sorting algorithum in python.
# It sorts the elements of the given collections based on the index position and values
# It always atarts with the 1st index position and it compares its previous element 
# If the previous elment is less than the present element it assings the lesser element 
# At the end of the inner loop it assings the least valuebased on the remain index position


#  Basic Implementation

# For sorting the elements in ascending order
# By default every sorting algorithms sorts int elements in ascending order
l=[3,8,-1,33,4,3,-10,10,2,-67]

for ind1 in range(1,len(l)):
    a=ind1
    val=l[a]
    while a >0 and val < l[a-1]:
        l[a]=l[a-1]
        a-=1
    l[a]=val
print(l)


# For sorting the elements in ascending order
l=[3,8,-1,33,4,3,-10,10,2,-67]

for ind1 in range(1,len(l)):
    a=ind1
    val=l[a]
    while a >0 and val > l[a-1]:
        l[a]=l[a-1]
        a-=1
    l[a]=val
print(l)

# In this algorithm it is difficult to find that after the completion of the first outer 
# for loop iteration which elements is  sorted first.
#  To get the complete sorting collection It should iterate all the iterations.
 