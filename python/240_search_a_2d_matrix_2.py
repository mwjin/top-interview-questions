from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row: List[int], target: int) -> bool:
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = low + (high - low) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        for row in matrix:
            if binarySearch(row, target):
                return True

        return False
