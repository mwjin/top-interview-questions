from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cell_set = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row_label = f"{i}({board[i][j]})"
                    col_label = f"({board[i][j]}){j}"
                    sub_box_label = f"{i // 3}({board[i][j]}){j // 3}"

                    if (
                        row_label in cell_set
                        or col_label in cell_set
                        or sub_box_label in cell_set
                    ):
                        return False

                    cell_set.add(row_label)
                    cell_set.add(col_label)
                    cell_set.add(sub_box_label)
        return True
