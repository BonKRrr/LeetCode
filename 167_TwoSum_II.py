class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers) - 1
        
        while i1 < i2:
            if numbers[i1] + numbers[i2] == target:
                ans = [i1 + 1, i2 + 1]
                break
            elif numbers[i1] + numbers[i2] < target:
                i1 += 1
            elif numbers[i1] + numbers[i2] > target:
                i2 -= 1

        return ans