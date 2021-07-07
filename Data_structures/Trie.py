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
    
    def search(self, word: str) -> bool:
        node = self.root 
        for letter in word: 
            if letter not in node.children: 
                return False 
            node = node.children[letter]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix: 
            if letter not in node.children: 
                return False 
            node = node.children[letter]
        return True 
        

