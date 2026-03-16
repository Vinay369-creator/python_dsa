# It is one of the sorting algorithm which is used to sort the all elements in ascending order by default.
# It  allows the duplicate values

#algorithm 

l=[2,6,12,-5,10,4]

# method 1
for index1 in range(len(l)-1):
    for index2 in range(0,len(l)-index1-1):
        if l[index2]>l[index2+1]:
            l[index2],l[index2+1]=l[index2+1],l[index2]

print(l)

#method 2
for index1 in range(len(l)-1,0,-1):
    for index2 in range(index1):
        if l[index2]>l[index2+1]:
            l[index2],l[index2+1]=l[index2+1],l[index2]

print(l)

# Sort in the descending order
for index1 in range(len(l)-1):
    for index2 in range(0,len(l)-index1-1):
        if l[index2]<l[index2+1]:
            l[index2],l[index2+1]= l[index2+1],l[index2]
print(l)


# Fetch the  first highest value from the list

for index1 in range(1):
    for index2 in range(0,len(l)-index1-1):
        if l[index2]>l[index2+1]:
            l[index2],l[index2+1]=l[index2+1],l[index2]
print(l[-1])


# Fetch the  second highest value from the list

for index1 in range(2):
    for index2 in range(0,len(l)-index1-1):
        if l[index2]>l[index2+1]:
             l[index2],l[index2+1]= l[index2+1],l[index2]
print(l[-2])

# fetch the first lowest value from the list

for index1 in range(1):
    for index2 in range(0,len(l)-index1-1):
        if l[index2]<l[index2+1]:
            l[index2],l[index2+1]= l[index2+1],l[index2]
print(l[-1])


# fetch the second lowest value from the list

for index1 in range(2):
    for index2 in range(0,len(l)-index1-1):
        if l[index2]<l[index2+1]:
            l[index2],l[index2+1]= l[index2+1],l[index2]
print(l[-2])


