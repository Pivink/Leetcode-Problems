def maximum_sub_array(nums):
    maxnum=float('-inf')
    current=0
    for num in nums:
        current+=num
        if current>maxnum:
            maxnum=current
        if current<0:
            current=0
    return maxnum
print(maximum_sub_array([-2,1,-3,4,-1,2,1,-5,4]))