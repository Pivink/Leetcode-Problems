def Difference(nums):
    if len(nums)<=4:
        return 0
    else:
        nums.sort()
    res=[]
    print(nums)
    for i in range(4):
        print(res)
        print(nums[len(nums)-4+i],nums[i])
        res.append(nums[len(nums)-4+i]-nums[i])
    return min(res)
print(Difference([1,5,0,10,14]))