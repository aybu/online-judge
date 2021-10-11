# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    """
        TC: O(logN)
        SC: O(1)
    """
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

