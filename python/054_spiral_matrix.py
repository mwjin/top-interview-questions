from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        col_begin, col_end = 0, len(matrix[0])
        row_begin, row_end = 0, len(matrix)
        matrix_size = len(matrix[0]) * len(matrix)

        while len(result) < matrix_size:
            for j in range(col_begin, col_end):
                result.append(matrix[row_begin][j])
            row_begin += 1

            for i in range(row_begin, row_end):
                result.append(matrix[i][col_end - 1])
            col_end -= 1

            if len(result) == matrix_size:
                break

            for j in range(col_end - 1, col_begin - 1, -1):
                result.append(matrix[row_end - 1][j])
            row_end -= 1

            for i in range(row_end - 1, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
            col_begin += 1

        return result


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder([[7], [9], [6]]))
