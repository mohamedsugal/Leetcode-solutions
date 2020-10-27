from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        # DO NOT RETURN ANYTHING
        # MODIFY IN-PLACE
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
        return nums1


def test():
    s = Solution()
    assert s.merge([0], 0, [1], 1) == [1]
    assert s.merge([2, 0], 1, [1], 1) == [1, 2]
    assert s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
