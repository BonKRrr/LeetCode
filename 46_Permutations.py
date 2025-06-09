class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums: List[int], level: int, permutations: List[List[int]]):
            if level == len(nums) - 1:
                permutations.append(nums[:]) 
                return
            for i in range(level, len(nums)):
                nums[i], nums[level] = nums[level], nums[i] 
                backtracking(nums, level + 1, permutations) 
                nums[i], nums[level] = nums[level], nums[i] 

    
        permutations = []

        backtracking(nums, 0, permutations)
        return permutations