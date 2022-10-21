from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def flip(row_idx: int, col_idx: int):
            if row_idx < 0 or row_idx == len(board):
                return
            if col_idx < 0 or col_idx == len(board[0]):
                return
            if board[row_idx][col_idx] != "O":
                return
            board[row_idx][col_idx] = "-"
            flip(row_idx - 1, col_idx)
            flip(row_idx + 1, col_idx)
            flip(row_idx, col_idx - 1)
            flip(row_idx, col_idx + 1)

        for row_idx in range(len(board)):
            flip(row_idx, 0)
            flip(row_idx, len(board[0]) - 1)
        for col_idx in range(len(board[0])):
            flip(0, col_idx)
            flip(len(board) - 1, col_idx)
        for m in range(len(board)):
            for n in range(len(board[m])):
                board[m][n] = "O" if board[m][n] == "-" else "X"


Solution().solve(
    [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
)
