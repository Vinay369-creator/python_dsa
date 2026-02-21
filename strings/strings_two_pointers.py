#reverse the characters
#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
s = ["h","e","l","l","o"]
def reverseStr(s):
    i=0
    j=len(s)-1
    while i<=j:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    return s
print(reverseStr(s))


#reverse  the only vowels in the given string
#Input: s = "IceCreAm"
#Output: "AceCreIm"
s = "IceCreAm"
def reverse(s):
    s=list(s)
    i=0
    j=len(s)-1
    v='aeiouAEIOU'
    while i<=j:
        if s[i] not in v:
            i+=1
        elif s[j] not in v:
            j-=1
        else:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
    return ''.join(s)
print(reverse(s))

#reverse on the words
#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"

s="Let's take LeetCode contest"
def wordReverse(s):
    l=list(map(lambda x : x[::-1],s.split()))
    return ' '.join(l)
print(wordReverse(s))

#reverse only the letters
#Input: s = "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"
s = "a-bC-dEf-ghIj"
def reverseOnlyLetters(s):
    s=list(s)
    i=0
    j=len(s)-1
    while i<=j:
        if not s[i].isalpha():
            i+=1
        elif not s[j].isalpha():
            j-=1
        else:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
    return ''.join(s)
print(reverseOnlyLetters(s))
