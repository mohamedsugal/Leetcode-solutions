from typing import List


class Solution:
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        # three pointers
        # first pointer will loop after the 2 other pointers traverse the
        # whole array except the first pointer
        # if we get the three numbers that sum up to specific number
        # add it to result
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        return result


arr = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.three_sum(arr))