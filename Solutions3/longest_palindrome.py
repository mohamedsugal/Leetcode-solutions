import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = collections.Counter(s)
        res = 0 
        for i in char_count.values(): 
            res += i // 2 * 2
            if res % 2 == 0 and i % 2 == 1: 
                res += 1
        return res
        
s = "ccc"
solution = Solution()
print(solution.longestPalindrome(s))
