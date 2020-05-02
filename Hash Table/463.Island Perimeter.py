# Solution 1:
# We scan the whole matrix, and every time we find a island,
# we first add 4 perimeters into results, and we need to check whether
# there exists island on the top or left of current island. If so,
# we subtract 2 duplicate perimeters.

# Time Complexity: O(N), where N is the total numbers of elements in grid.
# Space Complexity: O(N)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        res -= 2
        return res