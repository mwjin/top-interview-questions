from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Count the number of neighborhood
        for m in range(len(board)):
            for n in range(len(board[0])):
                num_neighbor = 0
                for i in range(max(0, m - 1), min(len(board), m + 2)):
                    for j in range(max(0, n - 1), min(len(board[0]), n + 2)):
                        num_neighbor += board[i][j] > 0
                num_neighbor -= board[m][n]
                # Positive if this is a live cell else negative
                # Adjusted by 10 to handle 0 due to lack of sign
                board[m][n] = (
                    num_neighbor + 10 if board[m][n] > 0 else -num_neighbor - 10
                )

        # Get the next state
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] in {-13, 12, 13}:
                    board[m][n] = 1
                else:
                    board[m][n] = 0


Solution().gameOfLife(
    [
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0],
    ]
)
