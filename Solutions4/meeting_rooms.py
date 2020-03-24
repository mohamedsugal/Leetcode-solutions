from typing import List


class Solution:
    @staticmethod
    def can_attend_meetings(intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


interval = [[0, 30], [5, 10], [15, 20]]
solution = Solution()
print(solution.can_attend_meetings(interval))
