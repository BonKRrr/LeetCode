class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = -sys.maxsize, 0
        for price in prices:
            buy = max(buy, -price)
            sell = max(sell, buy + price)
        return sell
