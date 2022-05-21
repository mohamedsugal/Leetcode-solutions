from typing import List


class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        node.isWord = True

    def LCP(self):
        prefix = []
        node = self.root
        while node:
            if node.isWord or len(node.children) > 1:
                break
            letter = list(node.children)[0]
            prefix.append(letter)
            node = node.children[letter]
        return "".join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        return trie.LCP()


strs = ["flower", "flow", "flowing"]
print(Solution().longestCommonPrefix(strs))
