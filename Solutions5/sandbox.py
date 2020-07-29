from typing import List
from collections import Counter


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket = Counter()
        fruits, i = float('-inf'), 0
        for idx, f in enumerate(tree):
            basket[f] += 1
            while len(basket) >= 3:
                basket[tree[i]] -= 1
                if basket[tree[i]] == 0:
                    del basket[tree[i]]
                i += 1
            fruits = max(fruits, idx - i + 1)
        print(fruits)


test = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
# test = [1, 2, 3, 2, 2]
solution = Solution()
solution.totalFruit(test)
