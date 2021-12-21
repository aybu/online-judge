from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            TC: O(N)?
            SC: O(1)
        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l, r = mid, mid
                while l > 0 and nums[l-1] == target:
                    l -= 1
                while r < n - 1 and nums[r+1] == target:
                    r += 1
                return l, r
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1, -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            TC: O(logN)
            SC: O(1)
        """
        start = self.get_leftmost_index(nums, target)
        end = self.get_rightmost_index(nums, target)

        if 0 <= start <= end < len(nums):
            return [start, end]
        return [-1, -1]

    def get_leftmost_index(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def get_rightmost_index(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r
        if 0 <= start <= end < len(nums):
            return [start, end]


s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))
assert s.searchRange(nums, target) == [3,4]

nums = [5,7,7,8,8,10]
target = 6
print(s.searchRange(nums, target))
assert s.searchRange(nums, target) == [-1,-1]

nums = []
target = 0
print(s.searchRange(nums, target))
assert s.searchRange(nums, target) == [-1,-1]

