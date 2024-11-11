def min_patches(nums, n):
    patches = 0
    missing = 1
    i = 0
    
    while missing <= n:
        if i < len(nums) and nums[i] <= missing:
            missing += nums[i]
            i += 1
        else:
            missing += missing
            patches += 1
    
    return patches

# Example usage
nums = [1,3]
n = 6
print(min_patches(nums, n))  # Output: 1
