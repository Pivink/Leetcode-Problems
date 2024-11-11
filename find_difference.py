def difference(s,t):
    # s=sorted(s)
    # t=sorted(t)
    res=""
    i,j=0,0,
    while i <(len(s)) and j<len(t):
        if s[i] != t[j]:
            res+=t[j]
        j+=1
        i+=1
    while j<len(t):
        res+=t[j]
        j+=1
    
    return res
s = ""
t = "a"
print(difference(s,t))