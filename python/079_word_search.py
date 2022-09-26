from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def track(row_idx, col_idx, word_idx) -> bool:
            if (
                row_idx < 0
                or row_idx == len(board)
                or col_idx < 0
                or col_idx == len(board[0])
            ):
                return False
            if board[row_idx][col_idx] != word[word_idx]:
                return False

            word_idx += 1
            if word_idx == len(word):
                return True

            original_char = board[row_idx][col_idx]
            board[row_idx][col_idx] = "-"  # Masking

            if (
                track(row_idx - 1, col_idx, word_idx)
                or track(row_idx + 1, col_idx, word_idx)
                or track(row_idx, col_idx - 1, word_idx)
                or track(row_idx, col_idx + 1, word_idx)
            ):
                return True

            board[row_idx][col_idx] = original_char
            return False

        for m in range(len(board)):
            for n in range(len(board[m])):
                if track(m, n, 0):
                    return True

        return False
