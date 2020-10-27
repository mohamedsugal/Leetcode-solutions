from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and self.dfs(board, i, j, rows, cols, 0, word):
                    return True
        return False

    def dfs(self, board, i, j, rows, cols, count, word):
        if count == len(word):
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[count]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        found = self.dfs(board, i + 1, j, rows, cols, count + 1, word) or \
            self.dfs(board, i - 1, j, rows, cols, count + 1, word) or \
            self.dfs(board, i, j + 1, rows, cols, count + 1, word) or \
            self.dfs(board, i, j - 1, rows, cols, count + 1, word)
        board[i][j] = temp
        return found


var = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
target = "ABCCED"
s = Solution()
print(s.exist(var, target))
