from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def findAnagrams(s: str, p: str) -> List[int]:
        res = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            s_count[s[i]] += 1  # include a new char in the window
            if s_count == p_count:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            s_count[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if s_count[s[i - len(p) + 1]] == 0:
                del s_count[s[i - len(p) + 1]]  # remove the count if it is 0
        return res


solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))
# print(solution.findAnagrams("abab", "ab"))
# print(solution.findAnagrams("baa", "aa"))
