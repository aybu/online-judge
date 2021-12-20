import math
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
            TC: O(N)
            SC: O(1)
        """
        arr.sort()
        ans = []
        min_diff = math.inf

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                ans = [[arr[i - 1], arr[i]]]
                min_diff = diff
            elif diff == min_diff:
                ans.append([arr[i - 1], arr[i]])

        return ans


s = Solution()
arr = [4,2,1,3]
print(s.minimumAbsDifference(arr))
assert s.minimumAbsDifference(arr) == [[1,2],[2,3],[3,4]]

arr = [1,3,6,10,15]
print(s.minimumAbsDifference(arr))
assert s.minimumAbsDifference(arr) == [[1,3]]

arr = [3,8,-10,23,19,-4,-14,27]
print(s.minimumAbsDifference(arr))
assert s.minimumAbsDifference(arr) == [[-14,-10],[19,23],[23,27]]

