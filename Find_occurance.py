def find_occurance(f,t):
    if not f:
        return -1
    if not t:
        return 0
    for i in range(len(f)):
        j=0
        while j<len(t) and i+j<len(f) and f[i+j]==t[j]:
            j+=1
        if j==len(t):
            return i
    return -1
def occurance(f,t):
    for i in range(len(f)-len(t)+1):
        if f[i:i+len(t)]==t:
            return i
    return -1
print(find_occurance("leetcode","leeto"))
print(occurance("butsosad","sad"))
s="   i am pivink   "
l=[]
r=""
print(len(r))