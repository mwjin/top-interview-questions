from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for offset in range(len(matrix) // 2):
            for row_idx in range(offset, len(matrix) - offset - 1):
                col_idx = offset
                temp = matrix[row_idx][col_idx]
                for _ in range(4):
                    row_idx, col_idx = col_idx, len(matrix) - row_idx - 1
                    matrix[row_idx][col_idx], temp = (
                        temp,
                        matrix[row_idx][col_idx],
                    )


m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(m)
print(m)
