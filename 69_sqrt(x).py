class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            mid_sqr = mid**2
            if mid_sqr == x:
                return mid
            if mid_sqr < x:
                l = mid + 1
            else:
                r = mid - 1
        return r