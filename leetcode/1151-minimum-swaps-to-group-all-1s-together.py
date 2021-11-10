from typing import List
import math

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
            idea: sliding window with two pointers
            TC: O(N), N: length of data
            SC: O(1)
        """
        size = len(data)
        min_swap = math.inf
        all_ones = sum(data)
        ones_in_window = 0
        left = 0

        for right in range(size):
            ones_in_window += data[right]
            if right - left == all_ones:
                ones_in_window -= data[left]
                left += 1

            min_swap = min(min_swap, all_ones - ones_in_window)

        return min_swap


s = Solution()
data = [1,0,1,0,1]
print(s.minSwaps(data)) # 1

data = [0, 0, 0, 1, 0]
print(s.minSwaps(data)) # 0

data = [1,0,1,0,1,0,0,1,1,0,1]
print(s.minSwaps(data)) # 3

