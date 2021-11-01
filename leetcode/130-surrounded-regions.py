from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            TC: O(m*n), m: #rows, n: #cols
            SC: O(m*n), m: #rows, n: #cols
        """
        # Idea: if any cell connecting to boarder, then it can not be flipped
        m, n = len(board), len(board[0])
        visited  = set()
        stack = []
        
        
        # Iterate boarder only
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    stack.append((i, j))

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    stack.append((i, j))

        # DFS
        while stack:
            x, y = stack.pop()
            visited.add((x, y))
            for nx, ny in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O' and  (nx, ny) not in visited :
                    stack.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'



s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
print(board) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

