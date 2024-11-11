def jump(l):
    ans,end,farthest=0,0,0
    for i in range(len(l)-1):
        farthest=max(farthest,i+l[i])
        if farthest>len(l)-1:
            ans+=1
            return ans
        if i==end:
            ans+=1
            end=farthest
    return ans
print(jump([2,3,1,1,4]))