from typing import List


class Solution:
    @staticmethod
    def missing_ranges(nums: List[int], lower, upper) -> List[str]:
        result = []
        nums.append(upper + 1)
        pre = lower - 1
        for i in nums:
            if i == pre + 2:
                result.append(str(i - 1))
            elif i > pre + 2:
                result.append(f'{str(pre + 1)}->{str(i - 1)}')
            pre = i
        return result


def test_solution():
    assert Solution.missing_ranges([0, 1, 3, 50, 75], 0, 99) == [
        "2", "4->49", "51->74", "76->99"]
    assert Solution.missing_ranges([3, 4, 6, 11, 20], 0, 70) == [
        "0->2", "5", "7->10", "12->19", "21->70"]
