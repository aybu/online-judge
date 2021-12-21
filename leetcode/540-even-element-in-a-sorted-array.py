from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
            TC: O(N)
            SC: O(1)
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans


    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
            TC: O(logN)
            SC: O(1)
        """
        n = len(nums)
        l, r = 0, n - 1

        while l < r: # use < instead of <= to avoid len(nums) == 1
            mid = l + (r - l) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid

        return nums[l]


s = Solution()
nums = [1,1,2,3,3,4,4,8,8]
assert s.singleNonDuplicate(nums) == 2
print(s.singleNonDuplicate(nums))

nums = [3,3,7,7,10,11,11]
assert s.singleNonDuplicate(nums) == 10
print(s.singleNonDuplicate(nums))

