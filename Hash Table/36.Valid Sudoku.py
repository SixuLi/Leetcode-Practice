# Solution 1: Hash Table

# Time Complexity: O(N^2), where N is the length of Sudoku.
# Space Complexity: O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        n = 9
        for i in range(n):
            Dict = dict()
            for j in range(n):
                if board[i][j] != '.' and board[i][j] in Dict:
                    return False
                else:
                    Dict[board[i][j]] = 1

        # Check each column
        for j in range(n):
            Dict = dict()
            for i in range(n):
                if board[i][j] != '.' and board[i][j] in Dict:
                    return False
                else:
                    Dict[board[i][j]] = 1

        # Check sub-boxes of the grid
        start_row = [0, 3, 6]
        start_col = [0, 3, 6]
        for row in start_row:
            for col in start_col:
                Dict = dict()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.' and board[i][j] in Dict:
                            return False
                        else:
                            Dict[board[i][j]] = 1
        return True