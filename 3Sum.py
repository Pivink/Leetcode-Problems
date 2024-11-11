def Sum_3(l):
    def backtrack(start,current):
        if len(current)==3 and sum(current)==0:
            current.sort()
            if current not in result:
                result.append(current[:])
            return
        elif len(current)>=3 and sum(current)!=0:
            return
        else:
            for i in range(start,len(l)):
                current.append(l[i])
                backtrack(i+1,current)
                current.pop()
    result=[]
    backtrack(0,[])
    return result
print(Sum_3([3,0,-2,-1,1,2]))