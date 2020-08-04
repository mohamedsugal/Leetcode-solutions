from typing import List


class Solution:
    @staticmethod
    def can_jump(nums: List[int]) -> bool:
        last_index = len(nums)-1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0


# arr = [3, 2, 1, 0, 4]
arr = [2, 3, 1, 1, 4]
# arr = [2, 0, 0]
s = Solution()
print(s.can_jump(arr))
