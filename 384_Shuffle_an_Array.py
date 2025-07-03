class Solution:

    def __init__(self, nums: List[int]):
        self.base = nums[:]

    def reset(self) -> List[int]:
        return self.base[:]

    def shuffle(self) -> List[int]:
        shuffled = self.base[:]
        n = len(self.base)
        for i in range(n - 1, -1, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()