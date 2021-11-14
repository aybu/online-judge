from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
            TC: O(N^2), N: length of students
            SC: O(1)
        """
        ns = len(students)
        pref = [0, sum(students)]
        pref[0] = ns - pref[1]

        while students:
            
            if (sandwiches[0] == 0 and pref[0] == 0) or (sandwiches[0] == 1 and pref[1] == 0):
                return len(students)
            
            if students[0] == sandwiches[0]:
                curr_pref = students.pop(0)
                sandwiches.pop(0)
                pref[curr_pref] -= 1
            else:
                students.append(students.pop(0))

        return 0


    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
            TC: O(2*N), N: length of students
            SC: O(1)
        """
        ns = len(students)
        k = 0
        pref_counts = Counter(students)

        while k < ns and pref_counts[sandwiches[k]]:
            pref_counts[sandwiches[k]] -= 1
            k += 1

        return ns - k


s = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(s.countStudents(students, sandwiches)) # 0

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(s.countStudents(students, sandwiches)) # 3

