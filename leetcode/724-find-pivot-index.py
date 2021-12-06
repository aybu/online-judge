from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
            TC: O(N)
            SC: O(N)
        """
        size = len(nums)
        prefix_sum = nums[:]
        suffix_sum = nums[:]

        for i in range(1, size):
            prefix_sum[i] += prefix_sum[i - 1]

        for i in range(size - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        for i in range(size):
            if prefix_sum[i] == suffix_sum[i]:
                return i

        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        """
            TC: O(N)
            SC: O(1)
        """
        size = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(size):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1


s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6])) # 3
print(s.pivotIndex([1, 2, 3])) # -1
print(s.pivotIndex([1])) # 0
print(s.pivotIndex([0])) # 0
print(s.pivotIndex([2, 1, -1])) # 0

