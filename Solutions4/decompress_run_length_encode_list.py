from typing import List


class Solution:
    @staticmethod
    def decompress_rle_list(nums: List[int]) -> List[int]:
        ans = []
        for i in range(1,len(nums),2):
            ans += [nums[i]]*nums[i-1]
        return ans


n = [1, 2, 3, 4]
s = Solution()
print(s.decompress_rle_list(n))