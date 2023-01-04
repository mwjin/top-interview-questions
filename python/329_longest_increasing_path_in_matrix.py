from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = 0
        cache = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def dfs(pos) -> int:
            if cache[pos[0]][pos[1]] != 0:
                return cache[pos[0]][pos[1]]

            result = 1
            m, n = pos
            v = matrix[m][n]

            if m > 0 and matrix[m - 1][n] > v:
                result = max(result, 1 + dfs((m - 1, n)))
            if m < len(matrix) - 1 and matrix[m + 1][n] > v:
                result = max(result, 1 + dfs((m + 1, n)))
            if n > 0 and matrix[m][n - 1] > v:
                result = max(result, 1 + dfs((m, n - 1)))
            if n < len(matrix[0]) - 1 and matrix[m][n + 1] > v:
                result = max(result, 1 + dfs((m, n + 1)))

            cache[pos[0]][pos[1]] = result
            return result

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                result = max(result, dfs((m, n)))

        return result


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
