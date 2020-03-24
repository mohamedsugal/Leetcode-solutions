class Solution(object): 
    def numberOfIslands(self, grid):
        islands_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1": 
                    islands_count += 1
                    self.DFS(grid, row, col)

        return islands_count

    def DFS(self, grid, row, col):
        # base cases:
        # 1) when row < 0 or row >= len(grid)
        # 2) when col < 0 or col >= len(grid[0])
        # 3) when current row, col == '0'
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0': 
            return 
        grid[row][col] = '0'
        self.DFS(grid, row - 1, col) # checking row down direction 
        self.DFS(grid, row + 1, col) # checking row up direction 
        self.DFS(grid, row, col - 1) # checking col left direction 
        self.DFS(grid, row, col + 1) # checking col right direction  

grid1 = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

grid2 = [["1", "1","0", "0", "0"],
         ["1", "1","0", "0", "0"],
         ["1", "1","1", "0", "0"],
         ["0", "0","0", "1", "1"]]

test = Solution()
print(test.numberOfIslands(grid1))
print(test.numberOfIslands(grid2))