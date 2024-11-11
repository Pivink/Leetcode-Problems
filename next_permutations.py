from bisect import bisect_right
def next_permutation(nums):
    if len(nums) == 1:
        return 
        
    i = len(nums) - 2
    x = nums
    while i >= 0 and x[i] >= x[i + 1]:
        i -= 1

    if i == -1:
        nums.sort()
    else:
        tail = x[i + 1:]
        tail.sort()

        j = bisect_right(tail, x[i])
        x[i], tail[j] = tail[j], x[i]
        x[i + 1:] = tail

# Example usage
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # Output: [1, 3, 2]