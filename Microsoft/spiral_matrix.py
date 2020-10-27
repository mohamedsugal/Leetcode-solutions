from typing import List


class Solution:
    @staticmethod
    def spiral_order(matrix: List[List[int]]) -> List[int]:
        result = []
        start_row = 0
        end_row = len(matrix) - 1
        start_col = 0
        end_col = len(matrix[0]) - 1
        direction = 0
        while start_row <= end_row and start_col <= end_col:
            if direction == 0:  # Right
                for i in range(start_col, end_col + 1):
                    result.append(matrix[start_row][i])
                start_row += 1
            elif direction == 1:  # down
                for i in range(start_row, end_row + 1):
                    result.append(matrix[i][end_col])
                end_col -= 1
            elif direction == 2:
                for i in range(end_col, start_col - 1, -1):
                    result.append(matrix[end_row][i])
                end_row -= 1
            elif direction == 3:
                for i in range(end_row, start_row - 1, -1):
                    result.append(matrix[i][start_col])
                start_col += 1
            direction = (direction + 1) % 4
        return result


nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
s = Solution()
print(s.spiral_order(nums))
