from typing import List


class Solution:
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        result = []  # Result list.
        for cur in intervals:
            if len(result) == 0:
                result.append(cur)
            else:
                prev = result[-1]
                if prev[1] >= cur[0]:  # Overlapped intervals.
                    prev[1] = max(prev[1], cur[1])
                else:
                    result.append(cur)

        return result


interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1,4],[4,5]]
# intervals = [[1,4],[5,6]]
# intervals = [[1,3]]
solution = Solution()
print(solution.merge(interval))
