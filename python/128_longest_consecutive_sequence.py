from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums = set(nums)

        for n in nums:
            if n - 1 not in nums:
                length = 0
                while n in nums:
                    length += 1
                    n += 1
                result = max(result, length)

        return result


Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
