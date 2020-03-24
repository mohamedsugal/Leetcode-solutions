import collections
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            elif t[i] in mapping.values(): 
                return False
            else:
                mapping[s[i]] = t[i]
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool: 
        s_map, t_map = {}, {}
        for c, c2 in zip(s, t): 
            if s_map.get(c, c2) != c2 or t_map.get(c2, c) != c: 
                return False
            s_map[c], t_map[c2] = c2, c
        return True


# s = "abba"
# t = "abab"

s = "aab"
t = "aaa"
solution = Solution()
print(solution.isIsomorphic(s, t))
