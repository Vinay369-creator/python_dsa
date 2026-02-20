s='hai python and data structure'
print(s[4]) # prints p

#slicing is nothing but extracting the multiple lements at a time
s='hai python and data structure'
print(s[::1])  # it prints the entire string

# print how many characters are present in the given string
s='hai python and data structure'
c=0
for i in s:
    if i.isalpha():
        c+=1
print(c)   

#sum the digits which is present in the given string
s='hai python 146747 structure'
sm=0
for i in range(len(s)):
    if s[i].isdigit():
        sm+=int(s[i])
print(sm)

# input  s='aabbcccdd'
#op='a2b2c3d2'

s='aabbcccdd'
res=''
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        c=1
res+=s[-1]+str(c)


s='a3b2c5'
#op=s='aaabbccccc'
new=''
for i in range(1,len(s),2):
    new+=s[i-1]*int(s[i])
print(new)


# check how many substrings are present'
s='hello worlldd'
ss='ll'
c=0
for i in range(len(s)-len(ss)):
    if ss==s[i:i+len(ss)]:
        c+=1
print(c)

#given input is 
#Input: s = "IceCreAm"
#Output: "AceCreIm"

def reversestr(rs):
    j=len(rs)-1
    s=list(rs)
    v='aeoiuAEIOU'
    i=0
    while i<=j:
        if s[j] not in v:
            j-=1
        elif s[i] not in v:
            i+=1
        else:
            s[j],s[i]=s[j],s[i]
            i+=1
            j-=1
    return ''.join(s)


#Input: strs = ["flower","flow","flight"]
#Output: "fl"
strs = ["flower","flow","flight"]
def longestsubstr(strs):
    least=min(strs,key=len)
    res=''
    for i in range(len(least)):
        curr=least[i]
        for j in strs:
            if curr !=j[i]:
                return res
        res+=curr
    return res

print(longestsubstr(strs))

