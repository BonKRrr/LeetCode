class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction = [-1, 0, 1, 0, -1]

        def dfs(points: Deque[Tuple[int, int]], grid: List[List[int]], i: int, j: int):
            m, n = len(grid), len(grid[0])
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 2:
                return
            if grid[i][j] == 0:
                points.append((i, j))
                return
            grid[i][j] = 2
            for k in range(4):
                dfs(points, grid, i + direction[k], j + direction[k + 1])

    
        m, n = len(grid), len(grid[0])
        points = collections.deque()

        flipped = False
        for i in range(m):
            if flipped:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(points, grid, i, j)
                    flipped = True
                    break

        level = 0
        while len(points) > 0:
            level += 1
            points_at_current_level = len(points)
            for _ in range(points_at_current_level):
                r, c = points.popleft()
                grid[r][c] = 2
                for k in range(4):
                    x, y = r + direction[k], c + direction[k + 1]
                    if x >= 0 and x < m and y >= 0 and y < n:
                        if grid[x][y] == 2:
                            continue
                        if grid[x][y] == 1:
                            return level
                        grid[x][y] = 2
                        points.append((x, y))
        return level
