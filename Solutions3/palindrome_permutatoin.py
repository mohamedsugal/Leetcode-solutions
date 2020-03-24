import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = collections.Counter(s)
        count = 0 
        for n in dic.values(): 
            if n % 2 != 0: 
                count += 1
            if count > 1: 
                return False
        return True

s = "code"
t = Solution()
print(t.canPermutePalindrome(s))