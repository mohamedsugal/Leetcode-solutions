from typing import List


class Solution:
    @staticmethod
    def check_straight_line(coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y1-y0) * (x-x0) != (y-y0) * (x1-x0):
                return False
        return True

# Formula:
# y1 - y0     y - y0    then we perform cris cross multiplication
# ------- !=  ------    to avoid dividing by zero. So the final formula
# x1 - x0     x - x0    = (y1-y0) * (x-x0) != (y-y0) * (x1-x0)


points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
s = Solution()
print(s.check_straight_line(points))
