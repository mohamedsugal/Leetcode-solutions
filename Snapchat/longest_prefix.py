class TrieNode: 
	def __init__(self, val): 
		self.val = val 
		self.children = {}
		self.is_word = False 

class Trie: 
	def __init__(self): 
		self.root = TrieNode("*")
	
	def insert(self, word): 
		curr_node = self.root
		for letter in word: 
			if letter not in curr_node.children: 
				curr_node.children[letter] = TrieNode(letter)
			curr_node = curr_node.children[letter]
		curr_node.is_word = True 
	
	def longestPrefix(self): 
		curr_node = self.root
		prefix = []
		while curr_node: 
			# if curr_node is_word or curr_node.children > 1 
			if curr_node.is_word or len(curr_node.children) > 1: 
				return "".join(prefix)
			letter = list(curr_node.children)[0]
			prefix.append(letter)
			curr_node = curr_node.children[letter]
		return "".join(prefix)
	
	
from typing import List 
class Solution: 
	def longestCommonPrefix(self, words: List[str]) -> str:
		trie = Trie()
		for word in words: 
			trie.insert(word)
		return trie.longestPrefix()

words = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(words))

