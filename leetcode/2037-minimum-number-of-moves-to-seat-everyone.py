from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
            TC: O(NlogN)
            SC: O(N)
        """
        n = len(seats)
        seats.sort()
        students.sort()
        
        return sum([abs(students[i] - seats[i])  for i in range(n)])


s = Solution()
seats = [3,1,5]
students = [2,7,4]
print(s.minMovesToSeat(seats, students))

