from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        num_heap = []
        for i in range(k - 1):
            heapq.heappush(num_heap, (-nums[i], i))

        result = []
        for i in range(len(nums) - k + 1):
            heapq.heappush(num_heap, (-nums[i + k - 1], i + k - 1))

            while num_heap[0][1] < i:
                heapq.heappop(num_heap)

            result.append(-num_heap[0][0])

        return result


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().maxSlidingWindow([1], 1))
print(Solution().maxSlidingWindow([7, 2, 4], 2))
print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
