class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
            TC: O(3^mn), m: #rows, n: #cols (not 4^mn as 1 direction is where we are from)
            SC: O(mn), m: #rows, n: #cols
        """
        # Idea: DFS, check only one island
        self.num_path = 0
        m, n = len(grid), len(grid[0])
        sx, sy  = 0, 0 # starting pos
        to_be_visited = 0


        for i in range(m):
            for j in range(n):
                if grid[i][j] > -1:
                    to_be_visited += 1
                
                if grid[i][j] == 1:
                    sx, sy = i, j
        
        def backtrack(r, c, to_be_visited):
            if grid[r][c] == 2 and to_be_visited == 1:
                self.num_path += 1
                return
            
            orig_val = grid[r][c]
            grid[r][c] = -2
            to_be_visited -= 1
            
            for x, y in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > -1:
                    backtrack(x, y, to_be_visited)
        
            grid[r][c] = orig_val
            
        backtrack(sx, sy, to_be_visited)
        return self.num_path
            
            
