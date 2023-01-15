from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self._original = list(nums)
        self._nums = nums

    def reset(self) -> List[int]:
        for i, n in enumerate(self._original):
            self._nums[i] = n
        return self._nums

    def shuffle(self) -> List[int]:
        random.shuffle(self._nums)
        return self._nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
