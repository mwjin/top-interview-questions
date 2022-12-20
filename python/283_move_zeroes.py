from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0
        for n in nums:
            if n != 0:
                nums[non_zero_idx] = n
                non_zero_idx += 1

        for i in range(non_zero_idx, len(nums)):
            nums[i] = 0
