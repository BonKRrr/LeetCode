class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        max_len = 0
        while len(cache) > 0:
            cur = next(iter(cache))
            cache.remove(cur)
            l, r = cur - 1, cur + 1
            while l in cache:
                cache.remove(l)
                l -= 1
            while r in cache:
                cache.remove(r)
                r += 1
            max_len = max(max_len, r - l - 1)
        return max_len