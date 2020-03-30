# Solution 1: DFS + Backtracking
# Important issue: sign the paths that has been visited when doing DFS.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[k]:
            return False
        cur = board[i][j]
        board[i][j] = '#'
        isexist = self.dfs(board, word, i + 1, j, k + 1) or self.dfs(board, word, i, j + 1, k + 1) or self.dfs(board,
                                                                                                               word,
                                                                                                               i - 1, j,
                                                                                                               k + 1) or self.dfs(
            board, word, i, j - 1, k + 1)
        board[i][j] = cur
        return isexist