def Peak(nums):
     
    n = len(nums)
    left, right = 1 , n 
    nums.insert(0, float('-inf'))
    nums.insert(n+1, float('-inf')) 
    while(left <= right):
        mid = (left + right)//2
        if (nums[mid] > nums[mid+1]):
            if(nums[mid] > nums[mid -1]):
                return mid -1
            else:
                right = mid -1
        else:
            left = mid +1

    return -1
        
print(Peak([1,2,3,1]))