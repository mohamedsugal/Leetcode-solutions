class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        s = s.split(" ")
        res = []
        for i in s:
            res.append(i[::-1])
        return " ".join(res)


string = "Let's take LeetCode contest"
t = Solution()
print(t.reverseWords(string))
