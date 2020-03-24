from typing import List


class Solution:
    # sorting       Time: O(nlogn)      Space: O(1)
    @staticmethod
    def smaller_number1(nums: List[int]) -> List[int]:
        indices = {}
        arr = sorted(nums)
        for i in reversed(range(len(arr))):
            indices[arr[i]] = i
        return [indices[i] for i in nums]

    # buckets       Time: O(1)          Space: O(1)
    @staticmethod
    def smaller_number2(nums: List[int]) -> List[int]:
        count = [0] * 102
        result = []
        for i in nums:
            count[i + 1] += 1
        print(count)
        for i in range(1, 102):
            count[i] += count[i - 1]
        return [count[i] for i in nums]


values = [8, 1, 2, 2, 3]
s = Solution()
print(s.smaller_number1(values))
