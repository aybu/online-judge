class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
            TC: O(N)
            SC: O(1)
        """
        alice, bob = 0, 0
        cnt_map = {'A': 0, 'B': 0}
        for char in colors:
            if char == 'A':
                cnt_map['A'] += 1
                bob += max(cnt_map['B'] - 2, 0)
                cnt_map['B'] = 0
            else:
                cnt_map['B'] += 1
                alice += max(cnt_map['A'] - 2, 0)
                cnt_map['A'] = 0

        bob += max(cnt_map['B'] - 2, 0)
        alice += max(cnt_map['A'] - 2, 0)
        
        return alice > bob
    
    def winnerOfGame(self, colors: str) -> bool:
        """
            TC: O(N)
            SC: O(1)
        """
        a, b = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        
        return a > b


s = Solution()
test_cases = [
    'AAABABB', 
    'AA', 
    'ABBBBBBBAAA'
]
for i, color in enumerate(test_cases):
    print(i, s.winnerOfGame(color), color)

