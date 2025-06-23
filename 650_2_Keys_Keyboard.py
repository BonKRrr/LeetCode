class Solution:
    def minSteps(self, n: int) -> int:

        dp = [0] * 2 + list(range(2, n + 1))
        for i in range(2, n + 1):
            for j in range(2, floor(sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i // j]

                    break
        return dp[n]        