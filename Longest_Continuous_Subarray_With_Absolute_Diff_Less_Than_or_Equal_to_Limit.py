def deff_less(nums,limit):
    left=0
    right=len(nums)-1
    count=0
    while left<=right:
        min_val=min(nums[left],nums[right])
        max_val=max(nums[left],nums[right])
        if max_val-min_val<=limit:
            left+=1
            count+=1
        else:
            right-=1
    return count
print(deff_less([10,1,2,4,7,2],5))