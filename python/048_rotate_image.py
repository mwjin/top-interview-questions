from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for col_idx in range(len(matrix)):
            for row_idx in range(col_idx + 1, len(matrix)):
                matrix[col_idx][row_idx], matrix[row_idx][col_idx] = (
                    matrix[row_idx][col_idx],
                    matrix[col_idx][row_idx],
                )


m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(m)
print(m)
