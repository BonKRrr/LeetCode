class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[sys.maxsize - 1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                else:
                    dp[i][j] = 0
        for i in range(m - 1, -1, -1): 
            for j in range(n - 1, -1, -1): 
                if mat[i][j] != 0:
                    if i < m - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if j < n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp