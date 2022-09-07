from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        currHeight = height[0]
        currWater = 0

        for i in range(1, len(height)):
            if height[i] >= currHeight:
                result += currWater
                currHeight = height[i]
                currWater = 0
            else:
                currWater += currHeight - height[i]

        currHeight = height[-1]
        currWater = 0

        for i in range(len(height) - 1, -1, -1):
            if height[i] > currHeight:
                result += currWater
                currHeight = height[i]
                currWater = 0
            else:
                currWater += currHeight - height[i]

        return result
