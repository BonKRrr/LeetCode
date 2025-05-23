class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = dict()
        for num, count in counts.items():
            if count in buckets:
                buckets[count].append(num)
            else:
                buckets[count] = [num]
        top_k = []
        for count in range(len(nums), 0, -1):
            if count in buckets:
                top_k += buckets[count]
                if len(top_k) >= k:
                    return top_k[:k]
        return top_k[:k]