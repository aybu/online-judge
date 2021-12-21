import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
            TC: O(logN)
            SC: O(1)
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        """
            TC: O(1)
            SC: O(1)
        """
        if n <= 0:
            return False
        return math.log2(n) == int(math.log2(n))

    def isPowerOfTwo(self, n: int) -> bool:
        """
            TC: O(1)
            SC: O(1)
        """
        if n <= 0:
            return False
        return n & (-n) == n


s = Solution()
n = 1
assert s.isPowerOfTwo(n) == True

n = 0
assert s.isPowerOfTwo(n) == False

n = 16
assert s.isPowerOfTwo(n) == True

n = 3
assert s.isPowerOfTwo(n) == False

