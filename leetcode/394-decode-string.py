class Solution:
    def decodeString(self, s: str) -> str:
        """
            TC: O(M), M: output size of string
            SC: O(M), M: output size of string
        """
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                # pop characters in between brackets
                letters = "" 
                while stack[-1] != "[":
                    letters = stack.pop() + letters
                stack.pop()

                # pop digits
                times = ''
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times

                stack.append(int(times) * letters)

        return "".join(stack)


sol = Solution()
s = "3[a]2[bc]"
assert sol.decodeString(s) == "aaabcbc"
print(sol.decodeString(s))

s = "3[a2[c]]"
assert sol.decodeString(s) == "accaccacc"
print(sol.decodeString(s))

s = "10[a2]"
assert sol.decodeString(s) == "a2a2a2a2a2a2a2a2a2a2"
print(sol.decodeString(s))

s = "2[abc]3[cd]ef"
assert sol.decodeString(s) == "abcabccdcdcdef"
print(sol.decodeString(s))

s = "abc3[cd]xyz"
assert sol.decodeString(s) == "abccdcdcdxyz"
print(sol.decodeString(s))

