# Solution 1: DFS

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        matrix = [["0" for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = board[i][j]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 'O' and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    self.dfs(matrix, r, c, m, n)
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "O":
                    board[r][c] = "X"

    def dfs(self, matrix, r, c, m, n):
        if r < 0 or r >= m or c < 0 or c >= n or matrix[r][c] == "X":
            return
        matrix[r][c] = "X"
        self.dfs(matrix, r - 1, c, m, n)
        self.dfs(matrix, r + 1, c, m, n)
        self.dfs(matrix, r, c - 1, m, n)
        self.dfs(matrix, r, c + 1, m, n)