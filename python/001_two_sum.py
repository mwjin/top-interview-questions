from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffToIdx = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffToIdx:
                return [diffToIdx[diff], i]
            diffToIdx[n] = i
