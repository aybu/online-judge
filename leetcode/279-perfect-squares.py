class Solution:
    def numSquares(self, n: int) -> int:
        """
            TC: O(n**1.5)
            SC: O(n)
        """
        squares = [i**2 for i in range(1, int(n ** 0.5) + 1)]
        size = len(squares)
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for sq in squares:
                if i < sq:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        
        return dp[-1]
