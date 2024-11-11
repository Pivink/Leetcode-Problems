def minimize_happiness(happyness,k):
    res=0
    i=0
    happyness.sort(reverse=True)
    while k>0:
        happyness[i]=max(0,happyness[i]-i)
        res+=happyness[i]
        i+=1
        k-=1
    return res
def minimize_2(happiness,k):
    res=0
    for i in range(k):
        val=happiness.pop()-i
        if val<=0:
            break
        res+=val
    return res
print(minimize_happiness([1,2,3],2))
print(minimize_2([1,2,3],2))