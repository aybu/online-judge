from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            Brute-Force
            TC: O(N^2), N: length of temperatures
            SC: O(1)
        """
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break      
        return ans


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            Monotonic Stack
            TC: O(N)
            SC: O(N) -> can be optimized to O(1)
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return ans


s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(temperatures)) # [1,1,4,2,1,1,0,0]

temperatures = [30,40,50,60]
print(s.dailyTemperatures(temperatures)) # [1,1,1,0]

temperatures = [30,60,90]
print(s.dailyTemperatures(temperatures)) # [1,1,0]

