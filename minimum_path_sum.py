def Minimum_path(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for i in range(n)]  
    dp[0][0] = grid[0][0]
    
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    
    for j in range(1, n):
        dp[j][0] = dp[j-1][0] + grid[j][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
    
    return dp[-1][-1]

print(Minimum_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
