
class Solution:
    def maxPower(self, s: str) -> int:
        """
            TC: O(N), N: len(s)
            SC: O(1)
        """
        power, cur_power = 1, 1
        prev = None

        for char in s:
            if char == prev:
                cur_power += 1
            else:
                cur_power = 1
            power = max(power, cur_power)
            prev = char
        return power


sol = Solution()
s = "leetcode"
print(sol.maxPower(s)) # 2

s = "abbcccddddeeeeedcba"
print(sol.maxPower(s)) # 5

s = "triplepillooooow"
print(sol.maxPower(s)) # 5

s = "hooraaaaaaaaaaay"
print(sol.maxPower(s)) # 11

s = "tourist"
print(sol.maxPower(s)) # 11

s = "cc"
print(sol.maxPower(s)) # 2

