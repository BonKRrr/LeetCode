class Solution:
    def trailingZeroes(self, n: int) -> int:

        def trailingZeroes1(n):
            return 0 if n == 0 else n // 5 + trailingZeroes1(n // 5)
        
        return trailingZeroes1(n)