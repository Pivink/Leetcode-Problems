def sum_4(nums, target):
    def backtrack(start, current):
        if len(current) == 4 and sum(current) == target:
            res.append(current[:])
            return
        elif len(current) > 4:
            return
        else:
            for i in range(start, len(nums)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

    nums.sort()  # Sort the input list to handle duplicates properly
    res = []
    backtrack(0, [])
    return res

# Test cases
print(sum_4([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(sum_4([2, 2, 2, 2, 2], 8))       # Output: [[2, 2, 2, 2]]
