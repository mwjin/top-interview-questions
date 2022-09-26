from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row_idx, col_idx, word_idx, visited=set()) -> bool:
            if word_idx == len(word):
                return True

            positions = []
            if row_idx > 0:
                positions.append((row_idx - 1, col_idx))
            if row_idx < len(board) - 1:
                positions.append((row_idx + 1, col_idx))
            if col_idx > 0:
                positions.append((row_idx, col_idx - 1))
            if col_idx < len(board[0]) - 1:
                positions.append((row_idx, col_idx + 1))

            for pos in positions:
                if (
                    pos not in visited
                    and board[pos[0]][pos[1]] == word[word_idx]
                ):
                    visited.add(pos)
                    if dfs(*pos, word_idx + 1, visited):
                        return True
                    visited.remove(pos)

            return False

        for m in range(len(board)):
            for n in range(len(board[m])):
                if board[m][n] == word[0]:
                    if dfs(m, n, 1, {(m, n)}):
                        return True

        return False
