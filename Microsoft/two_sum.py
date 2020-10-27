from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, n in enumerate(nums):
            if n in mapping:
                return [mapping[n], i]
            mapping[target - n] = i
        return []


nums = [3, 2, 4]
target = 6

s = Solution()
print(s.twoSum(nums, target))
