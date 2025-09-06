class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, cur_sum = 0, 0
        cache = {0: 1} 
        for num in nums:
            cur_sum += num
            count += cache.get(cur_sum - k, 0)
            cache[cur_sum] = cache.get(cur_sum, 0) + 1
        return count
