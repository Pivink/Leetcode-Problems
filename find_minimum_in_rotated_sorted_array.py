def Find_minimum(nums):
    start=0
    end=len(nums)-1
    while start<end:
        mid =(start+end)//2
        if nums[mid]>nums[end]:
            start=mid+1
        elif nums[mid]<nums[start]:
            end=mid
        else: end-=1
    return nums[start]
print(Find_minimum([2,2,3,0,1]))
