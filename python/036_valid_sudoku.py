from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(row_idx: int):
            digit_set = set()
            for col_idx in range(9):
                cell = board[row_idx][col_idx]
                if cell in digit_set and cell.isdigit():
                    return False
                else:
                    digit_set.add(cell)
            return True

        def isValidCol(col_idx: int):
            digit_set = set()
            for row_idx in range(9):
                cell = board[row_idx][col_idx]
                if cell in digit_set and cell.isdigit():
                    return False
                else:
                    digit_set.add(cell)
            return True

        def isValidSubBox(row_idx: int, col_idx: int):
            digit_set = set()
            for i in range(row_idx, row_idx + 3):
                for j in range(col_idx, col_idx + 3):
                    cell = board[i][j]
                    if cell in digit_set and cell.isdigit():
                        return False
                    else:
                        digit_set.add(cell)
            return True

        for i in range(9):
            if not isValidRow(i) or not isValidCol(i):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidSubBox(i, j):
                    return False
        return True
