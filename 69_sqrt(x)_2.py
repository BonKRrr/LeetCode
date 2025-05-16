class Solution:
    def mySqrt(self, x: int) -> int:
        t = x
        while t**2 > x:
            t = (t + x // t) // 2
        return t
