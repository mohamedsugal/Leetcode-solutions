from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # product_left = [1,1,2,6]
        # product_right = [24,12,4,1]
        if not nums:
            return []
        left = right = 1
        result = []
        for i in nums:
            result += [left]
            left *= i
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result


nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))
