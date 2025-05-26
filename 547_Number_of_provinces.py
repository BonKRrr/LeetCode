class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(isConnected: List[List[int]], city: int, visited: Set[int]):
            visited.add(city)
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and i not in visited:
                    dfs(isConnected, i, visited)

        count = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(isConnected, i, visited)
                count += 1
        return count
