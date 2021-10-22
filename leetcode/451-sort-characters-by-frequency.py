from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        """
            TC: O(NlogN), N: length of s
            SC: O(N), N: length of s
        """
        
        cnt_map = defaultdict(int)
        ans = ''
        for char in s:
            cnt_map[char] += 1
        
        for char in sorted(cnt_map, key=cnt_map.get, reverse=True):
            ans += char * cnt_map[char]
        
        return ans
    
    def frequencySort(self, s: str) -> str:
        """
            TC: O(N), N: length of s
            SC: O(N), N: length of s
        """
        
        cnt_map = defaultdict(int)
        for char in s:
            cnt_map[char] += 1
        
        bucket = [ [] for _ in range(max(cnt_map.values()) + 1)]
        for char, freq in cnt_map.items():
            bucket[freq].append(char) 

        ans = ''
        for i in range(len(bucket) - 1, 0, -1):
            for char in bucket[i]:
                ans += char * i
        
        return ans

s = Solution()
test_cases = ['tree', 'cccaaa', 'Aabb']
for case in test_cases:
    print(case, '->', s.frequencySort(case))

