class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def wrapper(nums, k):
            pivot_val = random.choice(nums)
            larger, equal, smaller = [], [], []
            for num in nums:
                if num > pivot_val:
                    larger.append(num)
                elif num < pivot_val:
                    smaller.append(num)
                else:
                    equal.append(num)
            if k <= len(larger):
                return wrapper(larger, k)
            if k > len(larger) + len(equal):
                return wrapper(smaller, k - len(larger) - len(equal))
            return pivot_val

        return wrapper(nums, k)
