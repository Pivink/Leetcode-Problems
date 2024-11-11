def combination(n,k):
    def backtrack(start,current):
        if len(current)==k:
            result.append(current[:])
            return
        else:
            for i in range(start,n+1):
                current.append(i)
                backtrack(i+1,current)
                current.pop()
    result=[]
    backtrack(1,[])
    return result
print(combination(4,3))