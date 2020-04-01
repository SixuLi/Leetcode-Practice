# Solution 1: Dynamic Programming
# Let dp[i][j] represent the minimum number of operations required to convert word1[0...i] to word[0...j].
#
# 1. If j == 0, dp[i][j] = i.
# 2. If i == 0, dp[i][j] = j.
# 3. If word1[i] == word2[j], dp[i][j] = dp[i-1][j-1].
# 4. If word1[i] != word2[j], dp = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1].

# Time Complexity: O(len(word1) * len(word2))
# Space Complexity: O(len(word1) * len(word2))

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [(n2+1)*[0] for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[n1][n2]