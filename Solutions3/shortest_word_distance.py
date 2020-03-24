from typing import List 

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = -1, -1 
        min_distance = float('inf')
        for i in range(len(words)): 
            if words[i] == word1: 
                idx1 = i 
            elif words[i] == word2: 
                idx2 = i 
            
            if idx1 != -1 and idx2 != -1: 
                min_distance = min(min_distance, abs(idx1 - idx2))
        
        return min_distance
 
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

test = Solution()
res = test.shortestDistance(words, word1, word2)
print(res)
