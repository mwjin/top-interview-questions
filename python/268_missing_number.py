from typing import List
from functools import reduce


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect_sum = len(nums) * (len(nums) + 1) // 2
        return reduce(lambda x, y: x - y, nums, expect_sum)
