from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
            TC:O(logN)
            SC:O(1)
        """
        n = len(letters)
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            curr = letters[mid]

            if ord(curr) <= ord(target):
                left = mid + 1
            else:
                right = mid - 1

        return letters[left % n]


s = Solution()
letters = ["c","f","j"]
target = "a"
print(s.nextGreatestLetter(letters, target)) # c

letters = ["c","f","j"]
target = "c"
print(s.nextGreatestLetter(letters, target)) # f

letters = ["c","f","j"]
target = "d"
print(s.nextGreatestLetter(letters, target)) # f

letters = ["e", "e", "e", "n", "n", "n"]
target = "e"
print(s.nextGreatestLetter(letters, target)) # n

