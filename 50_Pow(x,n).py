class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPow2(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            if n < 0:
                return 1 / myPow2(x, -n)
            if n % 2 != 0:
                return x * myPow2(x, n - 1)
            myPowSqrt = myPow2(x, n >> 1)
            return myPowSqrt * myPowSqrt
        return myPow2(x, n)