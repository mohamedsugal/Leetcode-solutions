from typing import List


class Solution:
    @staticmethod
    def jump_game(nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0


def test_jump_game():
    s = Solution()
    assert s.jump_game([2, 3, 1, 1, 4]) is True
    assert s.jump_game([2, 0, 0]) is True
    assert s.jump_game([3, 2, 1, 0, 4]) is False
