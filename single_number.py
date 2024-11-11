def singleNumber(nums):
        out = 0
        for x in nums:
            out ^= x
            print(out)
        return out
print(singleNumber( [2,2,1]))