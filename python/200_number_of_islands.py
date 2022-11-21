from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def traverse_land(row_idx, col_idx):
            grid[row_idx][col_idx] = "0"
            if row_idx > 0 and grid[row_idx - 1][col_idx] == "1":
                traverse_land(row_idx - 1, col_idx)
            if row_idx < len(grid) - 1 and grid[row_idx + 1][col_idx] == "1":
                traverse_land(row_idx + 1, col_idx)
            if col_idx > 0 and grid[row_idx][col_idx - 1] == "1":
                traverse_land(row_idx, col_idx - 1)
            if col_idx < len(grid[0]) - 1 and grid[row_idx][col_idx + 1] == "1":
                traverse_land(row_idx, col_idx + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    traverse_land(i, j)

        return result
