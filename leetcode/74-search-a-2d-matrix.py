from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            TC: O(logMN)
            SC: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        r_lo, r_hi = 0, m - 1
        c_lo, c_hi = 0, n - 1

        while r_lo <= r_hi:
            r_mid = r_lo + (r_hi - r_lo) // 2
            if target < matrix[r_mid][0]:
                r_hi = r_mid - 1
            elif target > matrix[r_mid][-1]:
                r_lo = r_mid + 1
            else:
                while c_lo <= c_hi:
                    c_mid = c_lo + (c_hi - c_lo) // 2
                    if target < matrix[r_mid][c_mid]:
                        c_hi = c_mid - 1
                    elif target > matrix[r_mid][c_mid]:
                        c_lo = c_mid + 1
                    else:
                        return True
                break
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            TC: O(logMN)
            SC: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            curr = matrix[mid // n][mid % n]
            if target < curr:
                hi = mid - 1
            elif target > curr:
                lo = mid + 1
            else:
                return True
        return False


s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
assert s.searchMatrix(matrix, target) == True

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
assert s.searchMatrix(matrix, target) == False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 1
assert s.searchMatrix(matrix, target) == True

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
assert s.searchMatrix(matrix, target) == False

