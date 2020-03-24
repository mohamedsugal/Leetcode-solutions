from typing import List


class Solution:
    def min_domino_rotations(self, arr1: List[int], arr2: List[int]) -> int:
        if arr1[0] == arr2[0]:
            return self.count(arr1, arr2, arr1[0])
        else:
            return max(self.count(arr1, arr2, arr1[0]), self.count(arr1, arr2, arr2[0]))

    @staticmethod
    def count(arr1: List[int], arr2: List[int], target: int) -> int:
        count_top = count_bottom = 0
        for i in range(len(arr1)):
            if arr1[i] != target and arr2[i] != target:
                return -1
            elif arr1[i] != target:
                count_top += 1
            elif arr2[i] != target:
                count_bottom += 1

        return min(count_top, count_bottom)


val1 = [2, 1, 2, 4, 2, 2]
val2 = [5, 2, 6, 2, 3, 2]
solution = Solution()
print(solution.min_domino_rotations(val1, val2))
