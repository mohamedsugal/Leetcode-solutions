from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    ans += end - start
                    end -= 1
                else:
                    start += 1
        return ans


arr = [2, 3, 4, 4]
#      i j + 2
s = Solution()
print(s.triangleNumber(arr))