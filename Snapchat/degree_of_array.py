from typing import List
import unittest


class Solution:
    @staticmethod
    def find_shortest_subarray(nums: List[int]) -> int:
        count, first_seen = {}, {}
        degree = min_subarray = 0

        for index, num in enumerate(nums):
            if num not in first_seen:
                first_seen[num] = index
            count[num] = count.get(num, 0) + 1
            if count[num] > degree:
                degree = count[num]
                min_subarray = index - first_seen[num] + 1
            elif count[num] == degree:
                min_subarray = min(min_subarray, index - first_seen[num] + 1)

        return min_subarray


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().find_shortest_subarray([1, 2, 2, 3, 1, 4, 2]), 6)

    def test2(self):
        self.assertEqual(Solution().find_shortest_subarray([1, 2, 2, 3, 1]), 2)

    def test3(self):
        self.assertEqual(Solution().find_shortest_subarray([1, 3, 2, 2, 3, 1]), 2)


if __name__ == "__main__":
    unittest.main()
