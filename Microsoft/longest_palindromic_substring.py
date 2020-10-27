class Solution:
    def longest_palindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            odd = self.expand_middle(s, i, i)
            even = self.expand_middle(s, i, i + 1)
            result = max(result, odd, even, key=len)
        return result

    @staticmethod
    def expand_middle(s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


s = "babad"
s2 = "cbbd"
solution = Solution()
print(solution.longest_palindrome(s))
