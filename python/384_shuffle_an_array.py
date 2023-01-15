from typing import List
import random


class Solution:
    def __init__(self, nums: List[int]):
        self._nums = nums

    def reset(self) -> List[int]:
        return self._nums

    def shuffle(self) -> List[int]:
        return random.sample(self._nums, len(self._nums))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
