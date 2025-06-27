class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell, s1, s2 = [0] * n, [0] * n, [0] * n, [0] * n
        s1[0] = buy[0] = -prices[0]
        sell[0] = s2[0] = 0
        for i in range(1, n):
            buy[i] = s2[i - 1] - prices[i]
            s1[i] = max(buy[i - 1], s1[i - 1])
            sell[i] = max(buy[i - 1], s1[i - 1]) + prices[i]
            s2[i] = max(s2[i - 1], sell[i - 1])

        return max(sell[n - 1], s2[n - 1])
