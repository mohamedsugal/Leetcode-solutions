from typing import List
import heapq


class Solution:
    @staticmethod
    def sort_odd(nums: List[int]) -> List[int]:
        # Created odd array to store odd numbers
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                # if current number is odd push it to array
                odd.append(nums[i])
                # set the odd number's position to 'inf'
                nums[i] = 'inf'
        # Sort tha array in a reverse order
        odd.sort(reverse=True)

        for i in range(len(nums)):
            # if current number is 'inf' set it to the odd number
            if nums[i] == 'inf':
                nums[i] = odd.pop()
        return nums

    def sort_odd2(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            if num % 2 == 1:
                # use min-heap to store the values
                heapq.heappush(heap, num)
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                # if num is odd pop from heap and set it to nums[i]
                nums[i] = heapq.heappop(heap)
        return nums


print(Solution().sort_odd([5, 3, 2, 8, 1, 4]))
# print(Solution().sort_odd2([2, 22, 37, 11, 4, 1, 5, 0]))
# print(Solution().sort_odd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
