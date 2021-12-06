from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
            TC: O(N)
            SC: O(1)
        """
        size = len(nums)
        max_num = max(nums)
        max_idx = nums.index(max(nums))

        for i in range(size):
            if max_idx != i and max_num < 2 * nums[i]:
                return -1

        return max_idx


s = Solution()
print(s.dominantIndex([3, 6, 1, 0])) # 1
print(s.dominantIndex([1, 2, 3, 4])) # -1
print(s.dominantIndex([1])) # 0

