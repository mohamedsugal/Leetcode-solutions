import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        alpha = [0] * 26
        for i in range(len(s)): 
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        for i in alpha: 
            if i != 0: 
                return False 
        return True 

s = "anagram"
t = "nagaram"
S = Solution()
print(S.isAnagram(s, t))