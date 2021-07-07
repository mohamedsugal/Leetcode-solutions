from typing import List, Dict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for r in range(rows): 
            for c in range(cols): 
                if board[r][c] == word[0] and self.dfs(board, r, c, 0, word): 
                    return True 
        return False 
    
    def dfs(self, board, r, c, i, word): 
        if i == len(word): 
            return True 
        rows, cols = len(board), len(board[0])
        if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c]: 
            return False
        temp = board[r][c]
        board[r][c] = "*" 
        found = self.dfs(board, r + 1, c, i + 1, word) or \
                self.dfs(board, r - 1, c, i + 1, word) or \
                self.dfs(board, r, c + 1, i + 1, word) or \
                self.dfs(board, r, c - 1, i + 1, word)
        board[r][c] = temp 
        return found
        

    

board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "SEE"
print(Solution().exist(board, word))