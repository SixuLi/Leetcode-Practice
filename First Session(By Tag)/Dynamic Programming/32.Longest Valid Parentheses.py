# Solution 1: Using Stack
# For every "(" encounted, we push its index onto stack.
# For every ")" encounted, we pop the topmost element and subtract the current element's index from the top element of the stack,
# which gives the length of the currently encounted valid string of parentheses. If while popping the element, the stack becomes
# empty, we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings,
# and return the length of the longest valid string at the end.
# Special case to pay attention: we initialized the stack by pushing -1 into it.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlen = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        maxlen = max(maxlen, i-stack[-1])
                    else:
                        stack.append(i)
        return maxlen

# Solution 2: Dynamic Programming
# We make use of a dp array where ith element of dp represents the length of the longest valid substring ending at ith index.
# There are two cases:
# 1. If s[i] == ")" and s[i-1] == "(", then dp[i] = dp[i-2] + 2
# 2. If s[i] == ")" and s[i-1] == ")", then dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = "#" + s
        n = len(s)
        dp = n * [0]
        for i in range(2,n):
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = dp[i-2] + 2
            elif s[i] == ")" and s[i-1] == ")":
                if s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
        return max(dp)
























