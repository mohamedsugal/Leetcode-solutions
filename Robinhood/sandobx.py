from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1-n, n, 2):
            res.append(i)
        return res


n = 3
s = Solution()
print(s.sumZero(n))