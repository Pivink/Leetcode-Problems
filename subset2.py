def subset(nums):
    res=[]
    subsets=[]
    def dfs(i):
        if i >= len(nums):
            if subsets not in res:
                res.append(subsets[:])
                return
        subsets.append(nums[i])
        dfs(i+1)
        subsets.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
        dfs(i+1)
    dfs(0)
    return sorted(res)
print(subset([1,2,2]))