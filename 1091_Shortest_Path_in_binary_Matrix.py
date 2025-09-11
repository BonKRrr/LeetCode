class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        dist = 0
        q = collections.deque()
        q.append((0, 0))
        grid[0][0] = -1 
        count = len(q)

        while count > 0:
            dist += 1

            while count > 0:
                count -= 1
                r, c = q.popleft()

                if r == m - 1 and c == n - 1:
                    return dist
                
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue

                        x, y = r + dx, c + dy

                        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 0:
                            continue

                        grid[x][y] = -1
                        q.append((x, y))
                        
            count = len(q)
        return -1
