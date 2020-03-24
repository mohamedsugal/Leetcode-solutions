from typing import List


class Solution:
    @staticmethod
    def find_numbers(nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
            else:
                continue
        return count


n = [12, 345, 2, 6, 7896]
s = Solution()
print(s.find_numbers(n))
