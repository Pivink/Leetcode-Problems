def subsetXORSum(nums):
        res = 0
        for num in nums:
            res |= num
        return res * (1 << (len(nums) - 1))
print(subsetXORSum([1,3]))