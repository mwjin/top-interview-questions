from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            areaWidth = right - left
            if height[left] < height[right]:
                areaHeight = height[left]
                left += 1
            else:
                areaHeight = height[right]
                right -= 1
            result = max(areaHeight * areaWidth, result)

        return result


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
