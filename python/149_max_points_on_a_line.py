from typing import List, Tuple, Optional
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(point1: List[int], point2: List[int]) -> Tuple[int]:
            delta_x = point1[0] - point2[0]
            delta_y = point1[1] - point2[1]
            sign = 1 if delta_x * delta_y >= 0 else -1
            delta_x, delta_y = abs(delta_x), abs(delta_y)
            delta_gcd = gcd(delta_x, delta_y)
            return (delta_x // delta_gcd * sign, delta_y // delta_gcd)

        result = 1

        for i in range(len(points) - 1):
            slopeCnt = defaultdict(int)
            for j in range(i + 1, len(points)):
                slopeCnt[slope(points[i], points[j])] += 1
            result = max(result, max(slopeCnt.values()) + 1)

        return result


print(Solution().maxPoints([[0, 0], [1, -1], [1, 1]]))
print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
