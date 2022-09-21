from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_set = set()
        zero_col_set = set()

        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[row_idx])):
                if matrix[row_idx][col_idx] == 0:
                    zero_row_set.add(row_idx)
                    zero_col_set.add(col_idx)

        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[row_idx])):
                if row_idx in zero_row_set or col_idx in zero_col_set:
                    matrix[row_idx][col_idx] = 0

        print(matrix)


Solution().setZeroes(
    [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
)
