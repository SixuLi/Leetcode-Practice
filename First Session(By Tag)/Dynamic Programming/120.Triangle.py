# Solution 1: Dynamic Programming(Top-down)

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = [[0 for i in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[-1])

# Solution 2: Dynamic Programming(Top-down) Modify the triangle directly

# Time Complexity: O(N^2)
# Space Complexity: O(1)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

# Solution 3: Dynamic Programming(Bottom-up)
# We start from the nodes on the bottom row; the min pathsums for these nodes are the values of the nodes
# themselves. From there, the min pathsum at the i-th node on the k-th row would be the lesser of the
# pathsums of its two children plus the value of itself, i.e.,
# dp[k][i] = min(dp[k+1][i], dp[k+1][i+1]) + triangle[k][i]

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = [[0 for i in range(len(row))] for row in triangle]
        dp[-1] = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]

# Solution 4: Dynamic Programming(Bottom-up) Modify the triangle directly

# Time Complexity: O(N^2)
# Space Complexity: O(1)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]

# Solution 5: Dynamic Programming(Bottom-up) O(N) space

# Time Complexity: O(N^2)
# Space Complexity: O(N)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]






















