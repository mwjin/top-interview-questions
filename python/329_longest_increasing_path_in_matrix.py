from typing import List
from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.result = 0
        graph = self.createGraph()

        def dfs(pos, path=[]):
            path.append(pos)

            if not graph[pos]:
                self.result = max(self.result, len(path))

            for next in graph[pos]:
                dfs(next, path)

            path.pop()

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                dfs((m, n))

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
