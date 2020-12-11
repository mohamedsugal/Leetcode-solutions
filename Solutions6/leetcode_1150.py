from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first = self.first(nums, 0, len(nums) - 1, target)
        last = self.last(nums, 0, len(nums) - 1, target)
        return last - first + 1 > len(nums) // 2

    @staticmethod
    def first(nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or target > nums[mid - 1]) and nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def last(nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if (mid == len(nums) - 1 or target < nums[mid + 1]) and nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


print(Solution().isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
print(Solution().isMajorityElement([10, 100, 101, 101], 101))
