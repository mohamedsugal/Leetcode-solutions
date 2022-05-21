from typing import List 
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): 
            return []
        p_count, s_count = {}, {}
        for letter in p: 
            p_count[letter] = p_count.get(letter, 0) + 1
        left = right = 0 
        result, k = [], len(p)
        while right < len(s): 
            s_count[s[right]] = s_count.get(s[right], 0) + 1
            if right >= k: 
                if s_count[s[left]] == 1: 
                    del s_count[s[left]]
                else: 
                    s_count[s[left]] -= 1
                left += 1
            if p_count == s_count: 
                result.append(left)
            right += 1
        return result
            
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
