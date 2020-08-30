from typing import List


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, rows, cols)
                    islands += 1
        return islands

    def dfs(self, grid, i, j, rows, cols):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j, rows, cols)  # DOWN
        self.dfs(grid, i - 1, j, rows, cols)  # UP
        self.dfs(grid, i, j + 1, rows, cols)  # RIGHT
        self.dfs(grid, i, j - 1, rows, cols)  # LEFT


matrix1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
matrix2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def test():
    s = Solution()
    assert s.num_islands(matrix1) == 1
    assert s.num_islands(matrix2) == 3
