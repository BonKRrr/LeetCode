class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_count, n = 0, len(points)
        for i, point1 in enumerate(points):
            cache = dict() 
            same_xy, same_y = 1, 1

            for point2 in points[i + 1 :]:
                if point1[1] == point2[1]:
                    same_y += 1
                    if point1[0] == point2[0]:
                        same_xy += 1

                else:
                    dx, dy = point1[0] - point2[0], point1[1] - point2[1]
                    cache[dx / dy] = cache.get(dx / dy, 0) + 1
                    
            max_count = max(max_count, same_y)

            for count in cache.values():
                max_count = max(max_count, same_xy + count)
        return max_count
