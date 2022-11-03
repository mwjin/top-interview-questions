from itertools import combinations
from typing import List, Tuple, Optional
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def slope(point1: List[int], point2: List[int]) -> Optional[int]:
            if point1[0] == point2[0]:
                return None
            return (point2[1] - point1[1]) / (point2[0] - point1[0])

        def xIntercept(point1: List[int], point2: List[int]) -> Optional[int]:
            if point1[1] == point2[1]:
                return None

            return (point1[0] * point2[1] - point2[0] * point1[1]) / (
                point2[1] - point1[1]
            )

        def yIntercept(point1: List[int], point2: List[int]) -> Optional[int]:
            if point1[0] == point2[0]:
                return None

            return (point1[1] * point2[0] - point2[1] * point1[0]) / (
                point2[0] - point1[0]
            )

        def getLine(
            point1: List[int], point2: List[int]
        ) -> Tuple[Optional[int]]:
            return (
                slope(point1, point2),
                xIntercept(point1, point2),
                yIntercept(point1, point2),
            )

        lineToPoints = defaultdict(set)

        for point1, point2 in combinations(points, 2):
            line = getLine(point1, point2)
            lineToPoints[line].add(tuple(point1))
            lineToPoints[line].add(tuple(point2))

        return len(max(lineToPoints.values(), key=len))


print(Solution().maxPoints([[0, 0], [1, -1], [1, 1]]))
#  print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
