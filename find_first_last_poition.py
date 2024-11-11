def find_position(nums, target):
    if target in nums:
        res = []
        i = nums.index(target)
        res.append(i)
        while i < len(nums) and nums[i] == target:   
            i += 1
        res.append(i - 1)   
        return res
    return [-1, -1]
print(find_position([5,7,7,8,8,10],8))
l=[1,2,3,4,5,6]
print(l.index(5))