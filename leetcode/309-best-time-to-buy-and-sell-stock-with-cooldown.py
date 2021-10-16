class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            TC: O(N), N: size of prices
            SC: O(1)
        """
        n = len(prices)
        rest, held, sold = 0, -prices[0], -math.inf
        
        for i in range(n):
            pre_sold = sold
            sold = held + prices[i]
            held = max(held, rest - prices[i])
            rest = max(rest, pre_sold)
 
        return max(rest, sold)
