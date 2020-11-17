class Solution:
    def longest_palindromic_substring(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            odd = self.explore(i, i, s)
            even = self.explore(i, i+1, s)
            result = max(result, odd, even, key=len)
        return result

    @staticmethod
    def explore(left: int, right: int, s: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


print(Solution().longest_palindromic_substring("babad"))
