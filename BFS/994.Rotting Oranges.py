# Solution 1: BFS

# Time Complexity: O(m*n), where m and n are the length of row and column of the given
# grid.
# Space Complexity: O(1)

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        level = 0
        while queue:
            cur_row, cur_col, level = queue.popleft()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in directions:
                next_row, next_col = cur_row + d[0], cur_col + d[1]
                if self.isValid(grid, next_row, next_col) and grid[next_row][next_col] == 1:
                    grid[next_row][next_col] = 2
                    queue.append((next_row, next_col, level + 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return level

    def isValid(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True
