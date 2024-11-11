def Minimum(nums):
    left=0
    m=float('inf')
    right=len(nums)-1
    while left<=right:
        mid = (left+right)//2
        if nums[left]<=nums[mid]:
            m=min(nums[left],m)
            left=mid+1
        else:
            m=min(nums[mid],m)
            right=mid-1
    return m
print(Minimum([1]))