from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
            BFS, marked visited grid as 2
            TC: O(MN), M:#rows, N:#cols
            SC: O(MN), M:#rows, N:#cols
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        while queue:
            r, c, d = queue.popleft()
            if r == n - 1 and c == n - 1:
                return d
            
            for x, y in ((r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 2
                    queue.append((x, y, d + 1))
        return -1


s = Solution()
grid = [[0,1],[1,0]]
print(s.shortestPathBinaryMatrix(grid)) # 2

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(s.shortestPathBinaryMatrix(grid)) # -1

grid = [[1,0,0],[1,1,0],[1,1,0]]
print(s.shortestPathBinaryMatrix(grid)) # 3

