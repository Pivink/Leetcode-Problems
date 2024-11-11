def single_number(nums): # Time complexity O(n*n)
    single=[]
    for i in nums:
        if nums.count(i)==1:
            single.append(i)
    return single
def single_number2(nums): # Time comlexity O(n)
    count={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    single=[i for i in nums if count[i]==1]
    return single
print(single_number2([1,2,1,3,2,5]))