class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = self.reverseNumber(x)
        if x != r: 
            return False
        return True

    def reverseNumber(self, x: int) -> int: 
        result = 0
        remaining = abs(x)
        while remaining != 0: 
            result *= 10
            result += remaining % 10
            remaining //= 10

        return result


    


x = -121
test = Solution()
res = test.isPalindrome(x)
print(res)