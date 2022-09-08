from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mask = 100001

        for i, n in enumerate(nums):
            if n <= 0 or n > len(nums):
                nums[i] = mask

        for n in nums:
            abs_n = abs(n)
            if abs_n != mask and nums[abs_n - 1] > 0:
                nums[abs_n - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1
