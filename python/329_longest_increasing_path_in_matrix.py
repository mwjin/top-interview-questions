from typing import List
from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.result = 0
        self.cache = [
            [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        ]
        graph = self.createGraph()

        def dfs(pos) -> int:
            if self.cache[pos[0]][pos[1]] != 0:
                return self.cache[pos[0]][pos[1]]

            result = 1

            for next in graph[pos]:
                result = max(result, 1 + dfs(next))

            self.cache[pos[0]][pos[1]] = result
            return result

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                self.result = max(self.result, dfs((m, n)))

        return self.result

    def createGraph(self) -> dict:
        graph = defaultdict(list)

        for m in range(len(self.matrix)):
            for n in range(len(self.matrix[0])):
                v = self.matrix[m][n]
                pos = (m, n)
                if m > 0 and self.matrix[m - 1][n] > v:
                    graph[pos].append((m - 1, n))
                if m < len(self.matrix) - 1 and self.matrix[m + 1][n] > v:
                    graph[pos].append((m + 1, n))
                if n > 0 and self.matrix[m][n - 1] > v:
                    graph[pos].append((m, n - 1))
                if n < len(self.matrix[0]) - 1 and self.matrix[m][n + 1] > v:
                    graph[pos].append((m, n + 1))

        return graph


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
