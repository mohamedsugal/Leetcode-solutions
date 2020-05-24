class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        mapping = {}
        start = 0
        for i, c in enumerate(s):
            if c in mapping:
                start = max(start, mapping.get(c)+1)
            if len(result) < i - start + 1:
                result = s[start:i+1]
            mapping[c] = i
        return result


s = "pwwkew"
S = Solution()
print(S.lengthOfLongestSubstring(s))
