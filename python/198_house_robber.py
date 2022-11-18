from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        amounts = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            amounts.append(max(nums[i] + amounts[i - 2], amounts[i - 1]))

        return amounts[-1]


print(Solution().rob([1, 2, 3, 1]))
