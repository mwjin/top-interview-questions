from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        self.buildings = buildings
        heights = [0 for _ in range(self.maxY + 1)]

        for x, y, h in self.buildings:
            for i in range(x, y + 1):
                heights[i] = max(heights[i], h)

        result = []
        if heights[0] > 0:
            result.append([0, heights[0]])

        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                result.append([i, heights[i]])
            elif heights[i] < heights[i - 1]:
                result.append([i - 1, heights[i]])

        result.append([len(heights) - 1, 0])

        return result

    @property
    def maxY(self) -> int:
        return max(self.buildings, key=lambda x: x[1])[1]
