# Solution 1: Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = (n+1)*[0]
        for i in range(n+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-2] + dp[i-1]
        return dp[n]