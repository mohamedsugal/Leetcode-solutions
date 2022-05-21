import collections
from collections import Counter
from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        window = Counter()
        for i, c in enumerate(s2):
            window[c] += 1
            if i >= len(s1):
                left = s2[i - len(s1)]
                if window[left] == 1:
                    del window[left]
                else:
                    window[left] -= 1
            if window == s1_counter:
                return True
        return False

    def longestOnes(self, nums: List[int], k: int) -> int:
        queue = collections.deque()
        j = 0
        max_ones = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                queue.append(i)
            while len(queue) > k:
                if nums[j] == 0:
                    queue.pop()
                j += 1
            max_ones = max(max_ones, i - j + 1)
        return max_ones


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()
    # print(s.checkInclusion(s1, s2))

    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(Solution().longestOnes(nums, k))
