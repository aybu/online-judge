from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
            TC: O(N), N: length of arr
            SC: O(N), N: length or arr
        """
        n = len(arr)
        seen = set()
        stack = [start]

        while stack:
            idx = stack.pop()
            seen.add(idx)
            if arr[idx] == 0:
                return True

            for next_idx in (idx + arr[idx], idx - arr[idx]):
                if next_idx not in seen and 0 <= next_idx < n:
                    stack.append(next_idx)

        return False


s = Solution()
arr = [4,2,3,0,3,1,2]
start = 5
print(s.canReach(arr, start)) # True

arr = [4,2,3,0,3,1,2]
start = 0
print(s.canReach(arr, start)) # True

arr = [3,0,2,1,2]
start = 2
print(s.canReach(arr, start)) # False

