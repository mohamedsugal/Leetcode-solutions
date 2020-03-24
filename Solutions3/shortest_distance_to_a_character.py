from typing import List 

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        distance = []
        prev = float('-inf')
        for i, char in enumerate(S): 
            if char == C: 
                prev = i 
            distance.append(i - prev)
        
        prev = float('inf')
        for i in range(len(S)-1, -1, -1): 
            if S[i] == C: 
                prev = i
            distance[i] = min(distance[i], prev - i)
        print(distance)


S = "loveleetcode"
C = 'e'
test = Solution()
test.shortestToChar(S, C)

