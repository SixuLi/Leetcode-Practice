# Solution 1: DFS

# Time Complexity: O(m*n).
# Space Complexity: O(m*n) for the worst case.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        self.maxArea = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.maxArea = max(self.dfs(grid, i, j, m, n), self.maxArea)
        return self.maxArea

    def dfs(self, grid, i, j, m, n):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.dfs(grid, i - 1, j, m, n) \
                   + self.dfs(grid, i + 1, j, m, n) \
                   + self.dfs(grid, i, j - 1, m, n) \
                   + self.dfs(grid, i, j + 1,m, n)
        return 0