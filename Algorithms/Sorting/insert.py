from typing import List


class Solution:
    @staticmethod
    def array_intersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        size = max(arr1, arr2, arr3, key=len)
        i = 0
        return []


arr_1 = [1, 2, 3, 4, 5]
arr_2 = [1, 2, 5, 7, 9]
arr_3 = [1, 3, 4, 5, 8]

obj = Solution()
obj.arraysIntersection(arr_1, arr_2, arr_3)