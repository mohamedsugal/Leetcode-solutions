from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        window = Counter()
        for i, c in enumerate(s2):
            window[c] += 1
            if i >= len(s1):
                left = s2[i - len(s1)]
                if window[left] == 1:
                    del window[left]
                else:
                    window[left] -= 1
            if window == s1_counter:
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
s = Solution()
print(s.checkInclusion(s1, s2))
