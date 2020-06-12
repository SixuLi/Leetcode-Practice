# Solution 1: Stack

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum, curString = 0, ''
        for ch in s:
            if ch == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif ch == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif ch.isdigit():
                curNum = 10 * curNum + int(ch)
            else:
                curString += ch
        return curString