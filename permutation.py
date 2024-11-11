def permu(nums):
    perm = []
    n = len(nums)

    print(nums)
    def backtrack(start):
        if start == n:
            perm.append(nums[:])
            print(perm)
        for i in range(start, n):
            print(nums,"--",start,"--",i)
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return perm

print(permu([1, 2, 3]))
