class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                    
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]

                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]

                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
                    
        return dp[m - 1][n - 1]

