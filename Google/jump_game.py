from typing import List
import unittest


class Solution:
    @staticmethod
    def jump_game(nums: List[int]) -> bool:
        last_index = len(nums)-1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0


class TestSolution(unittest.TestCase):
    def test_inputs(self):
        self.assertAlmostEqual(Solution.jump_game([2, 3, 1, 1, 4]), True)
        self.assertAlmostEqual(Solution.jump_game([3, 2, 1, 0, 4]), False)
        self.assertAlmostEqual(Solution.jump_game([2, 0, 0]), True)