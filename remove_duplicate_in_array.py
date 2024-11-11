def remove_duplicate(nums):
    if len(nums)<=2:
        return len(nums)
    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1
    return j
print(remove_duplicate([1,1,1,2,2,3]))