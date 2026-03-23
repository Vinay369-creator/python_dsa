# this sorting algorithm will works by taking the povit elements which is present in the first and it
# comapres and divides the list into the sub lists and inserts the elements which is small in the left list
# and large elements in the right list it calls the function until the base condition is true
# when the length of list is one or less than one it returns the same list to the previous call 
# there we concatenate the left list and povit element and right list and retuns to the previous call.
l=[44,2,65,-1,2,-10,44]

def quick(l):
    if len(l)<=1:
        return l
    povit=l[0]
    left=[no for no in l[1:] if no < povit]
    right=[no for no in l[1:] if no >=povit]
    print(f'povit {povit}   tihs is left {left}, thid id right {right}')
    return quick(left) + [povit] + quick(right)

l=quick(l)
#print(l)