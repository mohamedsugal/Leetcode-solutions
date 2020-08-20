import re


class Solution:
    @staticmethod
    def atoi(s: str) -> int:
        if len(s) == 0:
            return 0

        value = list(s.strip())

        sign = -1 if value[0] == '-' else 1

        if value[0] in ['-', '+']:
            del value[0]

        res, i = 0, 0
        while i < len(value) and value[i].isdigit():
            res = res * 10 + ord(value[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


test = Solution()
print(test.atoi("testing+42  word"))
