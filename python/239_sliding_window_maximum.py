from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for i, n in enumerate(nums):
            while window and nums[window[-1]] <= n:
                window.pop()
            while window and i - window[0] >= k:
                window.popleft()
            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])

        return result


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(Solution().maxSlidingWindow([1], 1))
print(Solution().maxSlidingWindow([7, 2, 4], 2))
print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
