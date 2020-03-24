from typing import List


class Solution:
    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        left = 1
        result = []
        for i in range(len(nums)):
            result += [left]
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result


vals = [1, 2, 3, 4]
solution = Solution()
print(solution.product_except_self(vals))
