# Solution 1: Stack

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Dict = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in Dict.values():
                stack.append(ch)
            else:
                if not stack or Dict[ch] != stack.pop():
                    return False
        return True if not stack else False