from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            TC: O(N), N: length of prices
            SC: O(1)
        """
        n = len(prices)
        profit = 0

        for idx in range(1, n):
            if prices[idx] > prices[idx - 1]:
                profit += prices[idx] - prices[idx - 1]

        return profit


s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 7
print(s.maxProfit([1,2,3,4,5])) # 4
print(s.maxProfit([7,6,4,3,1])) # 0

