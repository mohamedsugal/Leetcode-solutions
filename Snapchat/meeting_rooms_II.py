from typing import List
import unittest
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        # min-heap to store the end time
        heap = [intervals[0][1]]
        heapq.heapify(heap)
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return len(heap)


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)

    def test2(self):
        self.assertEqual(Solution().minMeetingRooms([[7, 10], [2, 4]]), 1)


if __name__ == "__main__":
    unittest.main()
