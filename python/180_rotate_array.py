from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return

        last_elements = nums[-k:]

        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]

        nums[:k] = last_elements
