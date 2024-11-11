def rank_transform(arr):
    dup=sorted(arr)
    d={}
    c=1
    for i in dup:
        if i not in d:
            d[i]=c
            c+=1
    return [d[x] for x in arr]
print(rank_transform([40,10,20,30]))