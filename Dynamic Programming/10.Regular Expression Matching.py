# Solution 1: Recursion

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in (s[0], '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# Solution 2: Dynamic Programming
# We can use dp[i][j] to save whether s[i:] and p[j:] match. So, we can implete a bottum-up DP.
# And the checking condition is the same as Solution 1.

# Time Complexity: O(SP), where S=len(s) and P=len(p)
# Space Complexity: O(SP)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and p[j] in (s[i], '.')
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]