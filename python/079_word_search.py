from typing import Counter, List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_cnt = Counter([ch for row in board for ch in row])
        word_cnt = Counter(word)

        for ch in word_cnt:
            if word_cnt[ch] > board_cnt[ch]:
                return False

        self.board = board
        self.word = (
            word[::-1] if board_cnt[word[0]] > board_cnt[word[-1]] else word
        )

        for m in range(len(board)):
            for n in range(len(board[m])):
                if self.track(m, n, 0):
                    return True

        return False

    def track(self, row_idx, col_idx, word_idx) -> bool:
        if (
            row_idx < 0
            or row_idx == len(self.board)
            or col_idx < 0
            or col_idx == len(self.board[0])
        ):
            return False
        if self.board[row_idx][col_idx] != self.word[word_idx]:
            return False

        word_idx += 1
        if word_idx == len(self.word):
            return True

        original_char = self.board[row_idx][col_idx]
        self.board[row_idx][col_idx] = "-"  # Masking

        if (
            self.track(row_idx - 1, col_idx, word_idx)
            or self.track(row_idx + 1, col_idx, word_idx)
            or self.track(row_idx, col_idx - 1, word_idx)
            or self.track(row_idx, col_idx + 1, word_idx)
        ):
            return True

        self.board[row_idx][col_idx] = original_char
        return False
