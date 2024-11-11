def permutation_sequence(n,k):
    l=[str(i) for i in range(1,n+1)]
    res=[]
    def backtrack(start):
        if start==n:
            res.append("".join(l[:]))
        for i in range(start,len(l)):
            l[start],l[i]=l[i],l[start]
            backtrack(start+1)
            l[start],l[i]=l[i],l[start]
    backtrack(0)
    print(res[k-1])
permutation_sequence(3,5)