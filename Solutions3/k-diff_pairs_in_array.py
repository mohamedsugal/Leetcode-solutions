from typing import List
import collections

class Solution:
    @staticmethod
    def find_pairs(nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        res = 0
        for i in count: 
            if k > 0 and i + k in count or k == 0 and count[i] > 1: 
                res += 1
        return res

nums = [1,2,3,4,5]
k = 1
t = Solution()
print(t.find_pairs(nums, k))
