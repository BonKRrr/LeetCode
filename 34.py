class Solution:    
    def lowerBound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
    def upperBound(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lower = self.lowerBound(nums, target)
        upper = self.upperBound(nums, target) - 1
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]
        return [lower, upper]