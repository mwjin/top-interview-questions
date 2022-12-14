from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[0]) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if matrix[0][mid] == target:
                return True
            elif matrix[0][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        start = min(low, high)
        if start < 0:
            return False

        for col_idx in range(start, -1, -1):
            low = 0
            high = len(matrix) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if matrix[mid][col_idx] == target:
                    return True
                elif matrix[mid][col_idx] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
