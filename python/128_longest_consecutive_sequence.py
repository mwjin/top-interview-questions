from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        result = 1
        length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                length += 1
            else:
                result = max(result, length)
                length = 1

        return max(result, length)


Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
