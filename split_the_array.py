def Split(arr):
    s=set(arr)
    dict={}
    sum=0
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for i in s:
        if dict[i]>2:
            return False
        sum+=dict[i]
    print(dict,s,sum,len(arr))
    return sum==len(arr)
print(Split([1,1,2,2,3,4]))
