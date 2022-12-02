from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = [(l, -h, r) for l, r, h in buildings] + [
            (r, 0, -1) for _, r, _ in buildings
        ]
        heights.sort()

        result = [[0, 0]]
        max_heap = [(0, float("inf"))]  # [Height, Right Position]
        for l, neg_h, r in heights:
            while l >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if neg_h < 0:
                heapq.heappush(max_heap, (neg_h, r))

            curr_max_height = -max_heap[0][0]
            if result[-1][1] != curr_max_height:
                result.append([l, curr_max_height])

        return result[1:]
