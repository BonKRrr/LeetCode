class Solution:

    def __init__(self, w: List[int]):
        self.cumsum = w[:]
        for i in range(1, len(w)):
            self.cumsum[i] += self.cumsum[i - 1]


    def pickIndex(self) -> int:
        val = random.randint(1, self.cumsum[-1])
        return bisect.bisect_left(self.cumsum, val, 0, len(self.cumsum))
