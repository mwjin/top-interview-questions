from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []

        for row in matrix:
            for n in row:
                heapq.heappush(maxHeap, -n)
                if len(heapq) > k:
                    heapq.heappop(maxHeap)

        return -maxHeap[0]
