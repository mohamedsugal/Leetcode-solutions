from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = {}
        self.wordEnd = False


class Trie:
    def __init__(self):
        self.root = TreeNode("*")

    def insert(self, word):
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TreeNode(c)
            curr = curr.children[c]
            if i == len(word) - 1:
                curr.wordEnd = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.wordEnd

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Solution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        result, trie = [], Trie()
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, [], result)
        return result

    def dfs(self, board, i, j, node, path, result):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        val = path+[board[i][j]]
        word = "".join(val)
        if not node.startsWith(word):
            return
        if node.search(word) and word not in result:
            result.append(word)
        temp = board[i][j]
        board[i][j] = "#"
        for x, y in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            self.dfs(board, i + x, j + y, node, val, result)
        board[i][j] = temp


matrix = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
targets = ["oath", "pea", "eat", "rain"]
matrix2 = [["a", "a"]]
targets2 = ["a"]
s = Solution()
print(s.find_words(matrix, targets))
