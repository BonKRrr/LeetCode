class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        dist = 0
        while diff != 0:
            dist += diff & 1
            diff = diff >> 1
        return dist
