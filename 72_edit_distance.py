class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + int(word1[i - 1] != word2[j - 1]),
                        dp[i][j - 1] + 1,
                        dp[i - 1][j] + 1,
                    )
        return dp[m][n]