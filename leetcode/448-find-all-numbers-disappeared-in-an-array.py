from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            TC: O(N), N: length of nums
            SC: O(N), N: length of nums
        """
        nums_count = Counter(nums)
        size = len(nums)

        return [i for i in range(1, size + 1) if i not in nums_count]
    

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            TC: O(N), N: length of nums
            SC: O(1)
        """
        size = len(nums)
        for i in range(size):
            target = abs(nums[i]) - 1
            if nums[target] > 0:
                nums[target] *= -1 
        return [i + 1 for i in range(size) if nums[i] > 0]
                

s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums)) # [5,6]

nums = [1,1]
print(s.findDisappearedNumbers(nums)) # [2]

