class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for _ in range(32):
            m = m << 1
            m += n & 1
            n = n >> 1
        return m