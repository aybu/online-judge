from typing import List
from collections import Counter

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
            TC: O(N)
            SC: O(N)
        """
        coin_map = Counter(position)
        min_cost = math.inf
        
        for i in (0, 1): # we can move all chips to either pos 0 or 1 as cost for moving +2 or -2 is 0
            cost = 0
            for j in coin_map:
                cost += coin_map[j] * ((j - i) % 2)
            
            min_cost = min(min_cost, cost)
    
        return min_cost

    def minCostToMoveChips(self, position: List[int]) -> int:
        """
            TC: O(N)
            SC: O(1)
        """
        cnt_even, cnt_odd = 0, 0
        for num in position:
            if num % 2 == 0:
                cnt_even += 1
            else:
                cnt_odd += 1
                
        return min(cnt_even, cnt_odd)


s = Solution()
print(s.minCostToMoveChips([1,2,3])) # 1
print(s.minCostToMoveChips([2,2,2,3,3])) # 2
print(s.minCostToMoveChips([1,1000000000])) # 1

