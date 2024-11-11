def Winner(n,k):
    l=[i for i in range(1,n+1)]
    i,c=0,1
    while len(l)!=1:
        if c==k:
            l.remove(l[i])
            c=1
        if i==n-1:
            i=-1
        i+=1
        c+=1
    print(l[0])
Winner(6,5)