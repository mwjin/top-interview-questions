from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0_is_zero = False
        row_size, col_size = len(matrix), len(matrix[0])

        for row in matrix:
            if row[0] == 0:
                col0_is_zero = True
                break

        for row_idx in range(row_size):
            for col_idx in range(1, col_size):
                if matrix[row_idx][col_idx] == 0:
                    matrix[row_idx][0] = matrix[0][col_idx] = 0

        for row_idx in range(row_size - 1, -1, -1):
            for col_idx in range(col_size - 1, 0, -1):
                if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                    matrix[row_idx][col_idx] = 0

        if col0_is_zero:
            for row in matrix:
                row[0] = 0

        print(matrix)


Solution().setZeroes(
    [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
)
