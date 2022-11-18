from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}

        def rob_helper(index: int) -> int:
            if index == len(nums):
                return 0
            if index == len(nums) - 1:
                return nums[-1]

            if index not in memory:
                memory[index] = max(
                    nums[index] + rob_helper(index + 2),
                    rob_helper(index + 1),
                )
            return memory[index]

        return rob_helper(0)
