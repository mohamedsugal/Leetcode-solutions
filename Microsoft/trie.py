class TreeNode:
    def __init__(self, v):
        self.val = v
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children:
                curr.children[char] = TreeNode(char)
            curr = curr.children[char]
            if i == len(word) - 1:
                curr.word_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
