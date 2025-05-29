class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(
            combinations: List[List[int]], pick: List[int], pos: int, n: int, k: int):
            if len(pick) == k:
                combinations.append(pick[:])
                return
            for i in range(pos, n + 1):
                pick.append(i) 
                backtracking(combinations, pick, i + 1, n, k) 
                pick.pop()

        combinations = []
        pick = []
        backtracking(combinations, pick, 1, n, k)
        return combinations
