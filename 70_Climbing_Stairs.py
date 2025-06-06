class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev = prev = cur = 1
        for _ in range(2, n + 1):
            cur = prev_prev + prev
            prev_prev = prev
            prev = cur
        return cur