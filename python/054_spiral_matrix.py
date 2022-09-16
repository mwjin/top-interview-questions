from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        height, width = len(matrix), len(matrix[0])
        start_row = start_col = 0

        while height > 0 and width > 0:
            for j in range(start_col, start_col + width):
                result.append(matrix[start_row][j])
            for i in range(start_row + 1, start_row + height):
                result.append(matrix[i][start_col + width - 1])

            if width < 2 or height < 2:
                break

            for j in range(start_col + width - 2, start_col - 1, -1):
                result.append(matrix[start_row + height - 1][j])
            for i in range(start_row + height - 2, start_row, -1):
                result.append(matrix[i][start_col])

            height -= 2
            width -= 2
            start_row += 1
            start_col += 1

        return result


print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder([[7], [9], [6]]))
