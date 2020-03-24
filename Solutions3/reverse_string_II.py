class Solution:
    @staticmethod
    def reverseStr(s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k): 
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
    
s = "abcdefg"
k = 4
test = Solution()
print(test.reverseStr(s, k)) 
