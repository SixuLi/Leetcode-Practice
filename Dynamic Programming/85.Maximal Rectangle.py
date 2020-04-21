# Solution 1: Dynamic Programming
# Let dp[i][j] represent the max length of all 1 sequence ends with column j, at the ith row.
# Transition formula:
# If matrix[i][j] == "0", dp[i][j] = 0.
# If matrix[i][j] == "1", dp[i][j] = dp[i][j-1] + 1

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [n*[0] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    if matrix[i][j] == "0":
                        dp[i][j] = 0
                    elif matrix[i][j] == "1":
                        dp[i][j] = 1
                else:
                    if matrix[i][j] == "0":
                        dp[i][j] = 0
                    elif matrix[i][j] == "1":
                        dp[i][j] = dp[i][j-1] + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                Len = float("inf")
                for k in range(i, m):
                    Len = min(Len, dp[k][j])
                    if Len == 0:
                        break
                    ans = max(ans, Len*(k-i+1))
        return ans