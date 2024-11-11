def increment(nums):
    move=0
    for i in range(len(nums)):
        count=0
        while nums.count(nums[i])>1:
            nums[i]+=1
            count+=1
        move+=count
    return move
print(increment([3,2,1,2,1,7]))