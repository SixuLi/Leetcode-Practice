# Solution 1: DFS
# Algorithm:
# Linear scan the 2d grid map, if we encounter a node contained a "1",
# then it is a root node that triggers a DFS. During DFS, every visited
# node should be set as "0" to mark as visited node. Count the number
# of root nodes that trigger DFS, this number would be the number of
# islands.

# Time Complexity: O(m*n), where m is the number of rows and n is the number of columns.
# Space Complexity: worst case O(m*n) in case that the grip map is
# filled with lands where DFS goes by m*n deep.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        nums_islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    nums_islands += 1
                    self.dfs(grid, r, c, m, n)
        return nums_islands

    def dfs(self, grid, r, c, m, n):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.dfs(grid, r - 1, c, m, n)
        self.dfs(grid, r + 1, c, m, n)
        self.dfs(grid, r, c - 1, m, n)
        self.dfs(grid, r, c + 1, m, n)
