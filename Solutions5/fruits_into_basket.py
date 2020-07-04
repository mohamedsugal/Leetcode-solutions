from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def total_fruit(tree: List[int]) -> int:
        basket = Counter()
        ans = i = 0
        for j, fruit in enumerate(tree):
            basket[fruit] += 1
            while len(basket) >= 3:
                basket[tree[i]] -= 1
                if basket[tree[i]] == 0:
                    del basket[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans


trees = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
solution = Solution()
print(solution.total_fruit(trees))
