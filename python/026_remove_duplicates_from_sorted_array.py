from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastValIdx = 0

        for i, n in enumerate(nums):
            if n > nums[lastValIdx]:
                nums[lastValIdx + 1], nums[i] = nums[i], nums[lastValIdx + 1]
                lastValIdx += 1

        return lastValIdx + 1
