from typing import List 

# https://leetcode.com/problems/longest-common-prefix/discuss/204779/Python-Trie-Clean-Implementation

class TrieNode: 
    def __init__(self, val): 
        self.val = val 
        self.children = {}
        self.is_word = False 

class Trie: 
    def __init__(self): 
        self.root = TrieNode("*")
    
    def insert(self, word: str) -> None: 
        node = self.root 
        for letter in word: 
            if letter not in node.children: 
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        node.is_word = True 
    
    def longest_prefix(self): 
        result = []
        node = self.root 
        while node: 
            # return when it reaches end of word or if there are more than 1 branch
            if node.is_word or len(node.children) > 1:
                return "".join(result)
            letter = list(node.children)[0]
            result.append(letter)
            node = node.children[letter]
        return "".join(result)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest): 
            for word in strs: 
                if ch != word[i]: 
                    return shortest[:i]
        return shortest

    def longestCommonTrie(self, strs: List[str]) -> str: 
        if not strs: 
            return ""
        trie = Trie()
        for word in strs: 
            trie.insert(word)
        return trie.longest_prefix()

strs = ["flower","flow","flight"]
# print(Solution().longestCommonPrefix(strs))
print(Solution().longestCommonTrie(strs))