from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        for row in matrix:
            result += row
        result.sort()
        return result[k - 1]
